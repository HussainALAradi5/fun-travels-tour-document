# WalletController

Base path `/api/wallet`. Source: `controllers/payment/WalletController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/wallet/config` | - | Get stripe config. | public | - | `Map<String, String>` |
| `POST /api/wallet/top-up` | `WalletTopUpService.processWalletTopUp` | The FAILED payment record is kept when the card is declined, so the attempt stays visible. | CUSTOMER, ADMIN, MANAGER, OWNER, EMPLOYEE | query `amount`, `method`, `gatewayToken` | `TransactionResponse` |
