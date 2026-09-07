# PaymentProcessingService

**File:** `src/main/java/com/server/server/services/Account/PaymentProcessingService.java`

## Methods

### processPayment(reservationId, PaymentMethod) -> Payment
Routes to correct processor based on method.

### processWalletPayment(reservationId, userId) -> Payment
Deducts from wallet balance.

### processStripePayment(reservationId, token) -> Payment
Processes via Stripe API.
