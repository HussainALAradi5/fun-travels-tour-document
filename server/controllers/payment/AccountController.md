# AccountController

Base path `/api/accounts/user/{userId}`. Source: `controllers/payment/AccountController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/accounts/user/{userId}/balance` | `AccountService.getAccountForViewer` | Wallet of a user, visible to that user and to administrators. | any signed-in user | - | `AccountResponse` |
| `GET /api/accounts/user/{userId}/history` | `AccountService.getAccountForViewer`, `AccountService.getTransactionHistory` | Wallet of a user, visible to that user and to administrators. | any signed-in user | - | `List<TransactionResponse>` |
