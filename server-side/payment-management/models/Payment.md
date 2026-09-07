# Payment Model

**Table:** `payments`
**File:** `src/main/java/com/server/server/Models/Payment.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| amount | BigDecimal | Not Null | Payment amount |
| paymentMethod | PaymentMethod | Not Null | CREDIT_CARD, PAYPAL, BANK_TRANSFER, CASH_AT_OFFICE, WALLET |
| status | PaymentStatus | Not Null | PENDING, COMPLETED, FAILED, REFUNDED |
| stripePaymentId | String | - | Stripe transaction ID |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| reservation | TourReservation | ManyToOne | Associated reservation |
| transactions | Transaction | OneToMany | Related transactions |
