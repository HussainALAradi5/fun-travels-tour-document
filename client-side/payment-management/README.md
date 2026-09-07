# Payment Management (Client)

## Components
- PaymentTable, PaymentDetails
- TransactionTable, TransactionDetails
- WalletTopUpModal, StripeCheckoutForm

## Services
- paymentService, transactionService, walletService

## Hooks
- usePayment, useTransaction, useWallet

## Routes
| Route | Page | Access |
|-------|------|--------|
| /payments | PaymentTablePage | Private |
| /transactions | TransactionTablePage | Private |
| /admin/payments | PaymentTablePage | ADMIN |
| /admin/transactions | TransactionTablePage | ADMIN |
