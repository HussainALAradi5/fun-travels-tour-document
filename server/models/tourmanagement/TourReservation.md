# TourReservation

Table `tour_reservations`. Inherits `BaseEntity`. Source: `models/tourmanagement/TourReservation.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `reservationNumber` | `String` |  unique, required |
| `tour` | `Tour` | ManyToOne required |
| `user` | `User` |   |
| `requestedSlots` | `Integer` |   |
| `totalPrice` | `BigDecimal` |   |
| `status` | `GenericStatus` |   |
| `tickets` | `List<Ticket>` | OneToMany  |
| `transactions` | `List<Transaction>` | OneToMany  |
| `payments` | `List<Payment>` | OneToMany  |
| `bookingDate` | `LocalDateTime` |   |
| `holdExpiresAt` | `LocalDateTime` |   |
