# TransactionController

Base path `/api/transactions`. Source: `controllers/payment/TransactionController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/transactions` | `TransactionService.filterTransactions` | Get transactions. | ADMIN, MANAGER, EMPLOYEE, CUSTOMER, OWNER | query `filter` | `PageResponse<TransactionResponse>` | 400, 401, 403 |
| `GET /api/transactions/{id}` | `TransactionService.getById` | Get by id. | ADMIN, MANAGER, EMPLOYEE, CUSTOMER, OWNER | - | `TransactionResponse` | 401, 403, 404 |
| `POST /api/transactions/manual-credit/{userId}` | `AccountService.getAccountByUserId`, `TransactionService.creditAccount` | The user's wallet, created on first use for accounts that predate wallets. | ADMIN | query `amount`, `description` | `TransactionResponse` | 400, 401, 403, 404, 409 |
