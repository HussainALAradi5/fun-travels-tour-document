# AccountController

Base path `/api/v1/accounts/user/{userId}`. Source: `controllers/payment/AccountController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/v1/accounts/user/{userId}/balance` | `AccountService.getAccountForViewer` | Wallet of a user, visible to that user and to administrators. | any signed-in user | - | `AccountResponse` | 401, 403, 404, 409 |
| `GET /api/v1/accounts/user/{userId}/history` | `AccountService.getAccountForViewer`, `AccountService.getTransactionHistory` | Wallet of a user, visible to that user and to administrators. | any signed-in user | - | `List<TransactionResponse>` | 401, 403, 404, 409 |
