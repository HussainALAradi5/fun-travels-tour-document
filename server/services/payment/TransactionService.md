# TransactionService

Source: `services/payment/TransactionService.java`.

## Business logic

- `creditAccount` / `debitAccount` require a positive amount; a debit larger than the balance fails with 409 `INSUFFICIENT_BALANCE`. Accounts carry `@Version`, so concurrent updates fail instead of losing money (409).
- `filterTransactions`: customers see their own wallet; agency staff see booking transactions of their agency; admins see all.

## Functions

### `Transaction getById(Integer id)`

**Runs in:** read-only transaction

### `Transaction creditAccount(Account account, BigDecimal amount, TransactionType type, String description, TourReservation reservation)`

**Runs in:** transaction

### `Transaction debitAccount(Account account, BigDecimal amount, TransactionType type, String description, TourReservation reservation)`

**Runs in:** transaction

### `PageResponse<Transaction> filterTransactions(TransactionFilterRequest filter)`

**Runs in:** read-only transaction
