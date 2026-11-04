# Ticket

Table `tickets`. Inherits `BaseEntity`. Source: `models/tourmanagement/Ticket.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `ticketNumber` | `String` |  unique, required |
| `tour` | `Tour` | ManyToOne required |
| `customer` | `User` | ManyToOne required |
| `assignedSeat` | `Seat` | ManyToOne  |
| `seatPriceModifier` | `BigDecimal` |   |
| `totalPrice` | `BigDecimal` |   |
| `bookingDate` | `LocalDateTime` |   |
| `isPaid` | `boolean` |   |
| `ticketStatus` | `TicketStatus` |   |
| `approvalStatus` | `GenericStatus` |   |
| `hasMealPlan` | `boolean` |  required |
| `selectedMeals` | `List<MealPlan>` | ManyToMany  |
| `reservation` | `TourReservation` | ManyToOne  |
| `basePrice` | `BigDecimal` |   |
| `discountPrice` | `BigDecimal` |   |
| `qrCode` | `String` |   |
| `barcode` | `String` |   |
