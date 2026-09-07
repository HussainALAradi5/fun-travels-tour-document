# WalletTopUpService

**File:** `src/main/java/com/server/server/services/Account/WalletTopUpService.java`

## Code

```java
@Transactional
public Transaction processWalletTopUp(BigDecimal amount, PaymentMethod method, String stripeToken) {
    if (amount == null || amount.compareTo(BigDecimal.ZERO) <= 0) {
        throw new IllegalArgumentException("Amount must be greater than zero.");
    }

    User currentUser = userService.getCurrentUser();
    Account userAccount = accountService.getAccountByUserId(currentUser.getId());

    Payment payment = Payment.builder()
            .amount(amount).currency("USD").method(method)
            .status(PaymentStatus.PENDING)
            .transactionId("TRX-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase())
            .paymentDate(LocalDateTime.now()).build();
    payment = paymentRepository.save(payment);

    try {
        int amountInCents = amount.multiply(new BigDecimal("100")).intValue();
        Map<String, Object> chargeParams = new HashMap<>();
        chargeParams.put("amount", amountInCents);
        chargeParams.put("currency", "usd");
        chargeParams.put("source", stripeToken);
        chargeParams.put("description", "Wallet Top-Up for " + currentUser.getEmail());

        Charge charge = Charge.create(chargeParams);

        if (charge.getPaid()) {
            payment.setStatus(PaymentStatus.COMPLETED);
            payment.setTransactionId(charge.getId());
            paymentRepository.save(payment);
            return transactionService.creditAccount(userAccount, amount, TransactionType.WALLET_TOP_UP, "Wallet Top-Up via Stripe", null);
        }
    } catch (CardException e) {
        payment.setStatus(PaymentStatus.FAILED);
        paymentRepository.save(payment);
        throw new RuntimeException("Card Declined: " + e.getMessage());
    } catch (StripeException e) {
        payment.setStatus(PaymentStatus.FAILED);
        paymentRepository.save(payment);
        throw new RuntimeException("Payment processing error: " + e.getMessage());
    }
}
```

## Methods

### processWalletTopUp(amount, method, stripeToken) -> Transaction

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| amount | BigDecimal | Amount to top up (in dollars) |
| method | PaymentMethod | Payment method |
| stripeToken | String | Stripe token from frontend |

**Returns:** Transaction entity for the top-up

**Business Logic:**
1. Validates amount > 0
2. Gets current user and their account
3. Creates PENDING Payment record
4. Converts dollars to cents for Stripe
5. Creates Stripe Charge with token
6. If paid: marks Payment as COMPLETED, credits account
7. If failed: marks Payment as FAILED

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| IllegalArgumentException | "Amount must be greater than zero." |
| RuntimeException | "Card Declined: {message}" |
| RuntimeException | "Payment processing error: {message}" |
| RuntimeException | "Payment succeeded but was not marked as paid by Stripe." |
