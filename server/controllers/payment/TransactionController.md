# TransactionController

Base path `/api/transactions`. Source: `controllers/payment/TransactionController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/transactions` | `TransactionService.filterTransactions` | Get transactions. | ADMIN, MANAGER, EMPLOYEE, CUSTOMER, OWNER | query `filter` | `PageResponse<TransactionResponse>` |
| `GET /api/transactions/{id}` | `TransactionService.getById` | Get by id. | ADMIN, MANAGER, EMPLOYEE, CUSTOMER, OWNER | - | `TransactionResponse` |
| `POST /api/transactions/manual-credit/{userId}` | `AccountService.getAccountByUserId`, `TransactionService.creditAccount` | Manual credit. | ADMIN | query `amount`, `description` | `TransactionResponse` |
