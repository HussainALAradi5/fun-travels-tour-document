# Transaction

Table `transactions`. Inherits `BaseEntity`. Source: `models/payment/Transaction.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `type` | `TransactionType` |  required |
| `amount` | `BigDecimal` |  required |
| `account` | `Account` | ManyToOne required |
| `payment` | `Payment` | ManyToOne  |
| `reservation` | `TourReservation` | ManyToOne  |
| `description` | `String` |   |
| `timestamp` | `LocalDateTime` |   |
