# Inventory Service

**Source:** `src/main/java/com/server/server/services/tourmanagement/InventoryService.java`

This service is the atomic boundary for tour capacity and physical-seat state.

## `reserve`

### Function signature

```java
public Tour reserve(Integer tourId, int quantity, List<Ticket> tickets)
```

### Purpose

Temporarily holds tour capacity and any selected physical seats while a reservation awaits payment.

### Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tourId` | `Integer` | Yes | Tour whose inventory is being reserved. |
| `quantity` | `int` | Yes | Number of places requested; must be positive. |
| `tickets` | `List<Ticket>` | No | Tickets containing optional selected seat IDs; `null` is treated as empty. |

### Return value

The locked and saved `Tour` with reduced `availableSlots`.

### Function logic

1. Lock the tour row.
2. Validate quantity and active tour status.
3. Compare quantity with available capacity.
4. Validate, lock, and hold selected seats.
5. Decrease available slots and save the tour.

### Business logic

- Only active tours are bookable.
- Capacity cannot become negative.
- Travelers in one booking cannot share a seat.
- A seat must be available and belong to the tour's transportation.

### Side effects

Updates the tour and marks selected seats `RESERVED` in one transaction.

### Exceptions

| Exception/code | Exact message | Condition |
|---|---|---|
| `WorkflowException` | `"Tour not found."` | Tour does not exist. |
| `WorkflowException` | `"Inventory quantity must be greater than zero."` | Quantity is not positive. |
| `TOUR_NOT_BOOKABLE` | `"This tour is not available for booking."` | Tour is not active. |
| `INSUFFICIENT_CAPACITY` | `"There are not enough places available for this booking."` | Capacity is insufficient. |
| `DUPLICATE_SEAT` | `"Each traveler must have a different seat."` | A seat ID appears twice. |
| `SEAT_NOT_AVAILABLE` | `"Seat {seatCode} is no longer available. Please choose another seat."` | Seat is unavailable. |
| `INVALID_SEAT_FOR_TOUR` | `"The selected seat does not belong to this tour's transportation."` | Seat belongs to another unit. |

### Authorization and transaction

Called through secured booking workflows. `@Transactional`; locking prevents concurrent overselling.

## `confirmSeats`

### Function signature

```java
public void confirmSeats(List<Ticket> tickets)
```

### Purpose

Converts held seats into final booked seats after successful payment.

### Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tickets` | `List<Ticket>` | No | Confirmed tickets; `null` and tickets without seats are ignored. |

### Return value

No value.

### Function logic

For every assigned seat, lock it, require `RESERVED` or `BOOKED`, set `BOOKED`, and save.

### Business logic

A seat cannot be confirmed unless the booking already holds it. Accepting `BOOKED` makes payment confirmation retry-safe.

### Side effects

Updates physical seat status.

### Exceptions

`WorkflowException`: `"Seat {seatCode} is not held by this booking."`; missing seats propagate `"Seat not found."`.

### Authorization and transaction

Called internally by payment finalization. `@Transactional` with seat locks.

## `release`

### Function signature

```java
public void release(Integer tourId, int quantity, List<Ticket> tickets)
```

### Purpose

Restores capacity and selected seats after cancellation or hold expiry.

### Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `tourId` | `Integer` | Yes | Tour receiving restored capacity. |
| `quantity` | `int` | Yes | Positive number of places to restore. |
| `tickets` | `List<Ticket>` | No | Tickets whose assigned seats should be released. |

### Return value

No value.

### Function logic

Lock the tour, validate quantity, add capacity capped at `maxCapacity`, make assigned seats `AVAILABLE`, and save.

### Business logic

Repeated release cannot increase inventory beyond tour capacity.

### Side effects

Updates tour availability and seat status.

### Exceptions

Propagates `"Tour not found."`, `"Seat not found."`, and `"Inventory quantity must be greater than zero."`.

### Authorization and transaction

Called internally by cancellation and expiry workflows. `@Transactional` with row locks.

## `validateAndHoldSeats`

### Function signature

```java
private void validateAndHoldSeats(Tour tour, List<Ticket> tickets)
```

### Purpose

Validates explicit seat selections and places their temporary holds.

### Parameters

`tour` is the locked target tour; `tickets` contains optional seat selections.

### Return value

No value.

### Function logic

Tracks unique IDs, locks each seat, validates status and transportation ownership, marks it reserved, saves it, and replaces the ticket's seat reference with the managed entity.

### Business logic

Enforces one traveler per seat and prevents cross-transport seat selection.

### Side effects

Writes seat state and ticket object references.

### Exceptions

Produces `DUPLICATE_SEAT`, `SEAT_NOT_AVAILABLE`, `INVALID_SEAT_FOR_TOUR`, or `"Seat not found."` as described above.

### Authorization and transaction

Private helper executed inside `reserve`'s transaction.

## `lockTour`

### Function signature

```java
private Tour lockTour(Integer tourId)
```

### Purpose

Retrieves a tour using the repository's locking query.

### Parameters

`tourId` is the required database identifier.

### Return value

The locked `Tour`.

### Function logic

Calls `findByIdWithLock` and unwraps the result.

### Business logic

Serializes competing inventory changes.

### Side effects

Acquires a database lock for the surrounding transaction.

### Exceptions

`WorkflowException`: `"Tour not found."`

### Authorization and transaction

Private transactional helper.

## `lockSeat`

### Function signature

```java
private Seat lockSeat(Integer seatId)
```

### Purpose

Retrieves a physical seat using the locking repository query.

### Parameters

`seatId` is the required database identifier.

### Return value

The locked `Seat`.

### Function logic

Calls `findByIdWithLock` and unwraps the result.

### Business logic

Prevents two reservations from claiming the same seat concurrently.

### Side effects

Acquires a database lock.

### Exceptions

`WorkflowException`: `"Seat not found."`

### Authorization and transaction

Private helper used inside service transactions.

## `requirePositive`

### Function signature

```java
private void requirePositive(int quantity)
```

### Purpose

Protects inventory arithmetic from zero or negative quantities.

### Parameters

`quantity` is the number being validated.

### Return value

No value.

### Function logic

Throws when `quantity <= 0`.

### Business logic

Inventory operations must represent a real number of places.

### Side effects

None.

### Exceptions

`WorkflowException`: `"Inventory quantity must be greater than zero."`

### Authorization and transaction

Private pure validation helper.

## `safeTickets`

### Function signature

```java
private List<Ticket> safeTickets(List<Ticket> tickets)
```

### Purpose

Normalizes an optional ticket collection.

### Parameters

`tickets` may be `null`.

### Return value

The original list or an empty immutable list.

### Function logic

Returns `List.of()` for `null`; otherwise returns the input.

### Business logic

Bookings may reserve capacity without explicit seat assignments.

### Side effects

None.

### Exceptions

None directly.

### Authorization and transaction

Private pure normalization helper.
