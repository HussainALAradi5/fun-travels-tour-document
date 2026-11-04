## Business logic

**Places.** `Tour.availableSlots` drops when a booking is held and rises when it is released (never above `maxCapacity`). Every change locks the tour row (`PESSIMISTIC_WRITE`), so concurrent bookings for one tour are serialized.

**Seats are per tour.** A vehicle can serve several tours on different dates. A seat is taken for a tour when an active (not cancelled) ticket **of that tour** holds it; the same seat stays free for the vehicle's other tours. The seat's stored status only records its physical condition: `MAINTENANCE` seats are never sold. Cancelling a ticket frees its seat without any extra update.

### `reserve(Integer tourId, int quantity, List<Ticket> tickets)`

1. Requires an ACTIVE tour and enough places.
2. Validates each explicitly chosen seat: same vehicle, not chosen twice in the request, not under maintenance, not already taken on this tour.
3. Gives travelers without a chosen seat the lowest free seat, skipping seats chosen by other travelers in the same request.
4. Lowers `availableSlots`. Any failure aborts the whole hold.

### `release(Integer tourId, int quantity, List<Ticket> tickets)`

Returns places to the tour. Callers mark the tickets cancelled, which frees their seats.

### `takenSeatIds(Integer tourId)` / `isSeatInUse(Integer seatId)`

Per-tour taken seats (for booking and the seat picker) and whether a seat is held by any active ticket of an unfinished tour (used to lock seat edits and maintenance).
