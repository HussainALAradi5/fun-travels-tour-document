# Payment Service

**Source:** `src/main/java/com/server/server/services/PaymentService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions |
|---|---|---|---|---|---|
| `public Payment getById(Integer id)` | Payment ID | Queries by ID. | Central payment lookup. | Payment; read-only. | `ResourceNotFoundException("Payment", id)`. |
| `public Payment executeTransaction(TourReservation res, PaymentMethod method)` | Reservation and method | Returns an existing completed payment or calls `createPayment`. | Idempotency prevents duplicate completed charges. | Existing/new payment; transactional. | Account/debit failures may propagate. |
| `private Payment createPayment(TourReservation res, PaymentMethod method)` | Reservation and payment method | Builds a pending USD payment; wallet debit completes synchronously; card and PayPal remain pending for a verified signed webhook. | A client-supplied provider reference can never prove payment. | Writes payment and possibly a wallet transaction. | `"Insufficient wallet balance."` and account lookup failures may propagate. |
| `public PageResponse<Payment> filter(PaymentFilterRequest filter)` | Owner/status/method/date/search/page/sort | Validates dates, builds specifications, and executes safe pagination. | A single date cannot be combined with a range; end date is inclusive via next-day exclusive bound. | Payment page; read-only. | `"Use either date or startDate/endDate, not both."`; range/pagination validation may propagate. |

## Detailed behavior and displayed errors

### `getById(Integer id)`

- **What should happen:** Return the persisted payment used by payment details and downstream reconciliation.
- **Displayed errors:** If it does not exist, display the standard `Payment` resource-not-found message with the requested ID.

### `executeTransaction(TourReservation reservation, PaymentMethod method)`

- **What should happen:** Return the existing completed payment for the reservation when one exists; otherwise create exactly one new payment attempt.
- **Processing:** Search for a completed payment tied to the reservation, short-circuit when found, or delegate to `createPayment` inside the transaction.
- **Business rules:** A retry must not charge a successfully paid reservation twice. Payment amount comes from the reservation's authoritative total, not a client-submitted amount.
- **Displayed errors:** An unfunded wallet displays `Insufficient wallet balance.` Missing account or reservation dependencies display their resource-specific message. Unexpected provider/storage failures display a safe payment failure and must not reveal stack traces.

### `createPayment(TourReservation reservation, PaymentMethod method)`

- **What should happen:** Create a USD payment with a generated transaction reference and the correct initial/final status for the selected method.
- **Processing:** Build a pending record, copy the reservation total, generate the reference, execute the wallet debit when applicable, mark deterministic demo methods complete, set the completion date when completed, and save.
- **Business rules:** Wallet payment is atomic with the account transaction. Credit-card and PayPal remain pending until a verified signed provider callback completes them. Unsupported/asynchronous methods remain pending.
- **Displayed errors:** Wallet balance failure displays `Insufficient wallet balance.` Missing account data displays its resource error. A provider failure should display `Payment could not be completed. Please try again.` and retain no false completed state.

### `filter(PaymentFilterRequest filter)`

- **What should happen:** Return a bounded page matching owner, status, method, free text, and either a single date or a date range.
- **Processing:** Validate mutually exclusive date inputs and chronological bounds, build composable specifications, apply an allow-listed sort, and map the result to `PageResponse<Payment>`.
- **Business rules:** `endDate` is inclusive to the user and implemented as a next-day exclusive boundary. Arbitrary entity properties cannot be supplied as sort fields.
- **Displayed errors:** Conflicting date modes display `Use either date or startDate/endDate, not both.` An invalid chronological range displays the shared date-range validation message. Pagination and sort errors display their shared validation messages.
