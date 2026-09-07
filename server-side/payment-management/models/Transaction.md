# Transaction Model

**Table:** `transactions`
**File:** `src/main/java/com/server/server/Models/Transaction.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| amount | BigDecimal | Not Null | Transaction amount |
| transactionType | TransactionType | Not Null | PAYMENT, REFUND, PARTIAL_REFUND, CANCELLATION_FEE, WALLET_TOP_UP, MANUAL_ADJUSTMENT, WITHDRAWAL |
| description | String | - | Transaction description |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| account | Account | ManyToOne | Associated account |
| payment | Payment | ManyToOne | Associated payment |
| reservation | TourReservation | ManyToOne | Associated reservation |
