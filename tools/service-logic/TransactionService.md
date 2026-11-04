## Business logic

- `creditAccount` / `debitAccount` require a positive amount; a debit larger than the balance fails with 409 `INSUFFICIENT_BALANCE`. Accounts carry `@Version`, so concurrent updates fail instead of losing money (409).
- `filterTransactions`: customers see their own wallet; agency staff see booking transactions of their agency; admins see all.
