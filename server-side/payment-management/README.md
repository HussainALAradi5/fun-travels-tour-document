# Payment Management

Handles financial transactions, payments, and wallet operations.

## Entities
- **Payment** - Payment record for a reservation
- **Transaction** - Ledger entry recording financial movements

## Services
- [PaymentService](services/PaymentService.md) - Payment execution and queries
- [TransactionService](services/TransactionService.md) - Transaction ledger
- [PaymentProcessingService](services/PaymentProcessingService.md) - Payment method routing
- [WalletTopUpService](services/WalletTopUpService.md) - Wallet balance top-up

## Endpoints
- [PaymentController](endpoints/PaymentController.md) - `/api/payments`
- [TransactionController](endpoints/TransactionController.md) - `/api/transactions`
- [WalletController](endpoints/WalletController.md) - `/api/wallet`

## Business Logic
- Payments support 5 methods: Credit Card, PayPal, Bank Transfer, Cash at Office, Wallet
- Wallet payments deduct from user balance immediately
- Stripe payments process via Stripe API
- All financial amounts use BigDecimal for precision
