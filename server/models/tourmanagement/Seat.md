# Seat

Table `seats`. Inherits `BaseEntity`. Source: `models/tourmanagement/Seat.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `seatCode` | `String` |  required |
| `chairType` | `ChairType` |   |
| `status` | `SeatStatus` |   |
| `seatPriceModifier` | `Double` |   |
| `transportation` | `Transportation` | ManyToOne  |
