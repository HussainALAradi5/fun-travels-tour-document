# SeatService

Source: `services/tourmanagement/SeatService.java`.

Seat records of a vehicle. A seat's stored status is its physical condition (`AVAILABLE` or `MAINTENANCE`); whether it is sold is answered per tour.

## Business logic

- `search` with `tourId` returns the tour's vehicle seats and reports seats held by the tour's active tickets as `BOOKED`; without it, the stored physical status is returned.
- With `tourId` and a status filter, the filter runs in the query (BOOKED = held by the tour's tickets; AVAILABLE = free and not under maintenance; MAINTENANCE = free and under maintenance), so page sizes and totals are right.
- Staff may only set `AVAILABLE` or `MAINTENANCE`; `RESERVED`/`BOOKED` come from tickets (`SEAT_STATUS_LOCKED`). A seat held by an active ticket cannot go to maintenance (`SEAT_IN_USE`).
- Chair type and price modifier are locked while the seat is held by an active ticket or the vehicle is assigned to an APPROVED or ACTIVE tour (`SEAT_LAYOUT_LOCKED`).
- Agency staff can only edit seats of their agency's vehicles.

## Functions

### `PageResponse<Seat> getAll(Integer page, Integer size, String sortDir)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `Seat getById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Seat not found | `ResourceNotFoundException` | 404 |

### `PageResponse<SeatResponse> search(SeatFilterRequest filter)`

**Purpose:** Lists seats. With `tourId` the seats of that tour's vehicle are returned and seats held by the tour's active tickets are reported as `BOOKED`.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Tour not found | `ResourceNotFoundException` | 404 |

### `Seat updateSeat(Integer id, SeatUpdateRequest updatedData)`

**Purpose:** Chair type and price can only change while no active booking or approved/active tour uses the seat.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Cannot change the type or price of a seat held by an active ticket. | `WorkflowException` `SEAT_IN_USE` | 409 |
| Seat layout is locked while the vehicle is assigned to an approved or active tour. | `WorkflowException` `SEAT_LAYOUT_LOCKED` | 409 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Seat not found | `ResourceNotFoundException` | 404 |
| Seats are reserved and booked through tickets; staff can only set AVAILABLE or MAINTENANCE. | `WorkflowException` `SEAT_STATUS_LOCKED` | 409 |
| This seat is held by an active ticket. Move or cancel the ticket first. | `WorkflowException` `SEAT_IN_USE` | 409 |

### `Seat updateStatus(Integer id, SeatStatus status)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Seat not found | `ResourceNotFoundException` | 404 |
| Seats are reserved and booked through tickets; staff can only set AVAILABLE or MAINTENANCE. | `WorkflowException` `SEAT_STATUS_LOCKED` | 409 |
| This seat is held by an active ticket. Move or cancel the ticket first. | `WorkflowException` `SEAT_IN_USE` | 409 |
