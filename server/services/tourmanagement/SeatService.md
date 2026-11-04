# SeatService

Source: `services/tourmanagement/SeatService.java`.

Seat records of a vehicle. A seat's stored status is its physical condition (`AVAILABLE` or `MAINTENANCE`); whether it is sold is answered per tour.

## Business logic

- `search` with `tourId` returns the tour's vehicle seats and reports seats taken on that tour as `BOOKED`; without it, the stored physical status is returned.
- Staff may only set `AVAILABLE` or `MAINTENANCE`; `RESERVED`/`BOOKED` come from tickets (`SEAT_STATUS_LOCKED`). A seat held by an active ticket cannot go to maintenance (`SEAT_IN_USE`).
- Chair type and price modifier are locked while the seat is held by an active ticket or the vehicle is assigned to an APPROVED or ACTIVE tour (`SEAT_LAYOUT_LOCKED`).
- Agency staff can only edit seats of their agency's vehicles.

## Functions

### `PageResponse<Seat> getAll(Integer page, Integer size, String sortDir)`

**Runs in:** read-only transaction

### `Seat getById(Integer id)`

**Runs in:** read-only transaction

### `PageResponse<SeatResponse> search(SeatFilterRequest filter)`

**Purpose:** Lists seats. With `tourId` the seats of that tour's vehicle are returned and seats held by the tour's active tickets are reported as `BOOKED`.

**Runs in:** read-only transaction

### `Seat updateSeat(Integer id, SeatUpdateRequest updatedData)`

**Purpose:** Chair type and price can only change while no active booking or approved/active tour uses the seat.

**Runs in:** transaction

### `Seat updateStatus(Integer id, SeatStatus status)`

**Runs in:** transaction
