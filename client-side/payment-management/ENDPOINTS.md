# Payment and Wallet Management Client API Usage Endpoints

This table is the feature-owned HTTP contract. Business rules and exception details are documented in this folder's service pages.

| ID | Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|---|
| EP-1 | `GET` | `/api/wallet/config` | Supply publishable payment configuration. | None | Controller configuration | `getStripeConfig` |
| EP-2 | `POST` | `/api/wallet/top-up` | Add externally paid funds to a wallet. | Amount, method, optional Stripe token | `WalletTopUpService` | `processWalletTopUp` |
| EP-3 | `POST` | `/api/payments/execute/{reservationId}` | Pay and finalize a held reservation. | Reservation ID and payment method | `TourReservationService` | `finalizeReservationWithPayment` |
| EP-4 | `GET` | `/api/payments` | Search payments by owner, status, method, or dates. | `PaymentFilterRequest` | `PaymentService` | `filter` |
| EP-5 | `GET` | `/api/payments/{id}` | View one authorized payment. | Payment ID | `PaymentService` | `getById` |
| EP-6 | `GET` | `/api/transactions` | Search account transactions. | `TransactionFilterRequest` | `TransactionService` | `filterTransactions` |
| EP-7 | `GET` | `/api/transactions/{id}` | View one authorized transaction. | Transaction ID | `TransactionService` | `getById` |
| EP-8 | `POST` | `/api/transactions/manual-credit/{userId}` | Apply an administrative wallet credit. | User ID, amount, description | `AccountService`, `TransactionService` | `getAccountByUserId`, `creditAccount` |

## Endpoint rules

- Authentication and role authorization are enforced by the server.
- Request validation occurs before business-state changes.
- Success and error responses use the shared API envelope.
- Collection endpoints use bounded pagination where supported.

