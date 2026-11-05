# TransactionService

Source: `services/payment/TransactionService.java`.

## Business logic

- `creditAccount` / `debitAccount` require a positive amount; a debit larger than the balance fails with 409 `INSUFFICIENT_BALANCE`. Accounts carry `@Version`, so concurrent updates fail instead of losing money (409).
- `filterTransactions`: customers see their own wallet; agency staff see booking transactions of their agency; admins see all.

## Functions

### `Transaction getById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Transaction not found | `ResourceNotFoundException` | 404 |
| You do not have permission to view this transaction. | `AccessDeniedException` | 403 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `Transaction creditAccount(Account account, BigDecimal amount, TransactionType type, String description, TourReservation reservation)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Credit amount must be greater than zero. | `IllegalArgumentException` | 400 |

### `Transaction debitAccount(Account account, BigDecimal amount, TransactionType type, String description, TourReservation reservation)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Debit amount must be greater than zero. | `IllegalArgumentException` | 400 |
| Insufficient wallet balance. | `WorkflowException` | 409 |

### `PageResponse<Transaction> filterTransactions(TransactionFilterRequest filter)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
