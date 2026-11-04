# PaymentService

Source: `services/payment/PaymentService.java`.

## Business logic

- `executeTransaction` reuses an existing COMPLETED payment for the reservation (idempotent retry); otherwise creates one. Wallet payments debit the wallet and complete immediately; card/PayPal/bank/cash stay PENDING.
- `getById` and `filter` are scoped: customers see payments of their reservations, agency staff those of their agency's tours, wallet top-up payments only admins.

## Functions

### `Payment getById(Integer id)`

**Runs in:** read-only transaction

### `Payment executeTransaction(TourReservation res, PaymentMethod method)`

**Purpose:** Creates and executes a transaction.

**Runs in:** transaction

### `PageResponse<Payment> filter(PaymentFilterRequest filter)`

**Purpose:** Dynamic filtering with Date support and DESC sorting.

**Runs in:** read-only transaction
