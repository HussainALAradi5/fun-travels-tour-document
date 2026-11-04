# Payment

Table `payments`. Inherits `BaseEntity`. Source: `models/payment/Payment.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `transactionId` | `String` |   |
| `method` | `PaymentMethod` |   |
| `status` | `PaymentStatus` |   |
| `amount` | `BigDecimal` |  required |
| `currency` | `String` |   |
| `paymentDate` | `LocalDateTime` |   |
| `reservation` | `TourReservation` | ManyToOne  |
| `transactions` | `List<Transaction>` | OneToMany  |
