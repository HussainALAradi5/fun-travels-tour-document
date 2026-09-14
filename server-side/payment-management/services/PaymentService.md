# Payment Service

**Source:** `src/main/java/com/server/server/services/PaymentService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions |
|---|---|---|---|---|---|
| `public Payment getById(Integer id)` | Payment ID | Queries by ID. | Central payment lookup. | Payment; read-only. | `ResourceNotFoundException("Payment", id)`. |
| `public Payment executeTransaction(TourReservation res, PaymentMethod method)` | Reservation and method | Returns an existing completed payment or calls `createPayment`. | Idempotency prevents duplicate completed charges. | Existing/new payment; transactional. | Account/debit failures may propagate. |
| `private Payment createPayment(TourReservation res, PaymentMethod method)` | Reservation and payment method | Builds pending USD payment and transaction ID; wallet debits the account; demo card/PayPal complete deterministically; other methods remain pending; saves. | Wallet must be funded; external methods are demo placeholders pending real signed webhooks. | Writes payment and possibly wallet transaction. | `"Insufficient wallet balance."` and account lookup failures may propagate. |
| `public PageResponse<Payment> filter(PaymentFilterRequest filter)` | Owner/status/method/date/search/page/sort | Validates dates, builds specifications, and executes safe pagination. | A single date cannot be combined with a range; end date is inclusive via next-day exclusive bound. | Payment page; read-only. | `"Use either date or startDate/endDate, not both."`; range/pagination validation may propagate. |
