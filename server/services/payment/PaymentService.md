# PaymentService

Source: `services/payment/PaymentService.java`.

## Business logic

- Bookings are paid from the wallet only. `executeTransaction` reuses an existing COMPLETED payment for the reservation (idempotent retry); otherwise it debits the wallet and completes at once.
- Any other method fails with 409 `PAYMENT_METHOD_UNSUPPORTED` ("top up your wallet by card, then pay"). There is no provider webhook to complete an external booking payment, so accepting one would leave it pending forever.
- `getById` and `filter` are scoped: customers see payments of their reservations, agency staff those of their agency's tours, wallet top-up payments only admins.

## Functions

### `Payment getById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Payment not found | `ResourceNotFoundException` | 404 |
| Only administrators can view wallet top-up payments. | `AccessDeniedException` | 403 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `Payment executeTransaction(TourReservation res, PaymentMethod method)`

**Purpose:** Creates and executes a transaction.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Bookings are paid from your wallet. Top up your wallet by card, then pay. | `WorkflowException` `PAYMENT_METHOD_UNSUPPORTED` | 409 |

### `PageResponse<Payment> filter(PaymentFilterRequest filter)`

**Purpose:** Dynamic filtering with Date support and DESC sorting.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Use either date or startDate/endDate, not both. | `IllegalArgumentException` | 400 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
