# InventoryService

Source: `services/tourmanagement/InventoryService.java`.

Tour places and seat holds.  <p>Places: `Tour.availableSlots` drops when a booking is held and rises when it is released. The tour row is locked for every change, so bookings for one tour are serialized.  <p>Seats: a vehicle can serve several tours on different dates, so a seat is taken <em>per tour</em> when an active (not cancelled) ticket of that tour holds it. The seat's own status only describes its physical condition: `MAINTENANCE` seats are never sold. Cancelling a ticket therefore frees its seat for that tour without touching other tours.

## Business logic

**Places.** The tickets are the source of truth: places left = `maxCapacity` minus the tour's tickets that are not cancelled. Each booking recounts them before checking capacity and stores the result in `Tour.availableSlots`; a release adds the places back (never above `maxCapacity`); `reconcileActiveTours` recounts every ACTIVE tour nightly, so a drifted counter is corrected. Every change locks the tour row (`PESSIMISTIC_WRITE`), so concurrent bookings for one tour are serialized.

**Seats are per tour.** A vehicle can serve several tours on different dates. A seat is taken for a tour when an active (not cancelled) ticket **of that tour** holds it; the same seat stays free for the vehicle's other tours. The seat's stored status only records its physical condition: `MAINTENANCE` seats are never sold. Cancelling a ticket frees its seat without any extra update.

### `reserve(Integer tourId, int quantity, List<Ticket> tickets)`

1. Requires an ACTIVE tour and enough places, counted from its tickets (not from the stored counter).
2. Validates each explicitly chosen seat: same vehicle, not chosen twice in the request, not under maintenance, not already taken on this tour.
3. Gives travelers without a chosen seat the lowest free seat, skipping seats chosen by other travelers in the same request.
4. Lowers `availableSlots`. Any failure aborts the whole hold.

### `release(Integer tourId, int quantity, List<Ticket> tickets)`

Returns places to the tour. Callers mark the tickets cancelled, which frees their seats.

### `takenSeatIds(Integer tourId)` / `isSeatInUse(Integer seatId)`

Per-tour taken seats (for booking and the seat picker) and whether a seat is held by any active ticket of an unfinished tour (used to lock seat edits and maintenance).

## Functions

### `Tour reserve(Integer tourId, int quantity, List<Ticket> tickets)`

**Purpose:** Holds places and seats. Tickets without a chosen seat get the lowest free seat.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| This tour is not available for booking. | `WorkflowException` `TOUR_NOT_BOOKABLE` | 409 |
| There are not enough places available for this booking. | `WorkflowException` `INSUFFICIENT_CAPACITY` | 409 |
| Inventory quantity must be greater than zero. | `WorkflowException` | 409 |
| Tour not found. | `WorkflowException` | 409 |
| This tour has no transportation seats to choose. | `WorkflowException` `INVALID_SEAT_FOR_TOUR` | 409 |
| Seat not found. | `WorkflowException` `SEAT_NOT_FOUND` | 409 |
| The selected seat does not belong to this tour's transportation. | `WorkflowException` `INVALID_SEAT_FOR_TOUR` | 409 |
| Each traveler must have a different seat. | `WorkflowException` `DUPLICATE_SEAT` | 409 |
| Seat   is no longer available. Please choose another seat. | `WorkflowException` `SEAT_NOT_AVAILABLE` | 409 |
| No standard seats are left on this tour. Please choose a seat for each traveler. | `WorkflowException` `SEAT_CHOICE_REQUIRED` | 409 |

### `int reconcileActiveTours()`

**Purpose:** Nightly: sets every bookable tour's available places from its tickets.

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `void release(Integer tourId, int quantity, List<Ticket> tickets)`

**Purpose:** Returns places to the tour. Seats free themselves once their tickets are cancelled.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Inventory quantity must be greater than zero. | `WorkflowException` | 409 |
| Tour not found. | `WorkflowException` | 409 |

### `Set<Integer> takenSeatIds(Integer tourId)`

**Purpose:** Ids of seats held by active tickets of the tour.

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `boolean isSeatInUse(Integer seatId)`

**Purpose:** True when a seat is held by an active ticket of any tour that has not finished.

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.
