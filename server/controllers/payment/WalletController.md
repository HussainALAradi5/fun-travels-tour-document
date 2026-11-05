# WalletController

Base path `/api/v1/wallet`. Source: `controllers/payment/WalletController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/v1/wallet/config` | - | Get stripe config. | public | - | `Map<String, String>` | - |
| `POST /api/v1/wallet/top-up` | `WalletTopUpService.processWalletTopUp` | The FAILED payment record is kept when the card is declined, so the attempt stays visible. | CUSTOMER, ADMIN, MANAGER, OWNER, EMPLOYEE | query `amount`, `method`, `gatewayToken` | `TransactionResponse` | 400, 401, 403, 409 (`CARD_DECLINED`, `PAYMENT_FAILED`, `PAYMENT_NOT_CAPTURED`) |
