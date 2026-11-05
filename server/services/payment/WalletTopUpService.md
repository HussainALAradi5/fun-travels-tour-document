# WalletTopUpService

Source: `services/payment/WalletTopUpService.java`.

## Business logic

Card only (`CREDIT_CARD`) with a Stripe token. The amount is converted to cents exactly; a declined or uncaptured charge fails with 409 and the wallet is not credited, but the FAILED payment record is kept (`noRollbackFor`) so the attempt stays visible. A successful charge records the Stripe charge id and credits the wallet.

## Functions

### `Transaction processWalletTopUp(BigDecimal amount, PaymentMethod method, String stripeToken)`

**Purpose:** The FAILED payment record is kept when the card is declined, so the attempt stays visible.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Amount must be greater than zero. | `IllegalArgumentException` | 400 |
| Wallet top-ups are only supported by card. | `IllegalArgumentException` | 400 |
| A card token is required. | `IllegalArgumentException` | 400 |
| The card payment was not captured. | `WorkflowException` `PAYMENT_NOT_CAPTURED` | 409 |
| Card declined: | `WorkflowException` `CARD_DECLINED` | 409 |
| Payment processing error: | `WorkflowException` `PAYMENT_FAILED` | 409 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
