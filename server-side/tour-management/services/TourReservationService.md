# Tour Reservation Service

**Source:** `src/main/java/com/server/server/services/tourmanagement/TourReservationService.java`

This service coordinates booking holds, group-ticket pricing, payment finalization, cancellation refunds, inventory, notifications, and customer data isolation.

## `getAll(page, size, sortDir)`

### Function signature

```java
public PageResponse<TourReservation> getAll(Integer page, Integer size, String sortDir)
```

### Parameters

`page` is the zero-based page, `size` is the requested page size, and `sortDir` is `asc` or `desc`.

Returns reservations ordered by booking date. Customers are automatically restricted to their own reservations; operational roles receive the complete requested page.

## `getById(id)`

### Function signature

```java
public TourReservation getById(Integer id)
```

### Parameters

`id` (`Integer`, required) is the reservation identifier.

Retrieves a reservation and applies customer ownership authorization.

Failures: `"Reservation not found"` or `"You are not authorized to access this reservation."`

## `sendTravelReminders()`

### Function signature

```java
public void sendTravelReminders()
```

### Parameters

None.

Finds confirmed reservations whose tour starts one week from the current date and sends a `ONE_WEEK_TRAVEL_REMINDER` containing the tour title and reservation number.

## `create(reservation)`

### Function signature

```java
public TourReservation create(TourReservation res)
```

### Parameters

`res` is the requested reservation aggregate, including customer/tour references, requested slots, and optional tickets, seats, and meals.

Access: customer, employee, admin, or manager.

Logic:

1. Force customer users to book for their authenticated identity.
2. Require a customer identifier for staff-created reservations.
3. Load the managed tour and reject overlapping active reservations.
4. Derive requested slots from ticket count, then `requestedSlots`, then one.
5. Generate a `RES-XXXXXXXX` number, set `PENDING`, and create a 15-minute hold.
6. Generate each ticket's codes and resolve its seat and meals.
7. Calculate ticket and reservation totals.
8. Atomically reserve tour capacity and selected seats.
9. Save and notify the customer to complete payment.

Failures:

| Exact message | Condition |
|---|---|
| `"A reservation customer is required."` | No valid customer is supplied. |
| `"At least one ticket is required."` | Derived slot quantity is not positive. |
| `"You already have an active reservation that conflicts with these dates."` | Customer has an overlapping booking. |
| `"Failed to generate ticket codes for group booking: {reason}"` | QR/barcode generation fails. |
| `"Meal '{mealName}' is not offered on this tour."` | A selected meal is outside the tour catalog. |

Inventory error codes may propagate: `TOUR_NOT_BOOKABLE`, `INSUFFICIENT_CAPACITY`, `DUPLICATE_SEAT`, `SEAT_NOT_AVAILABLE`, and `INVALID_SEAT_FOR_TOUR`.

## Ticket pricing helper

`processTicketsAndCalculateTotal` applies:

```text
ticket total = tour total price - ticket discount + seat modifier + selected meal prices
reservation total = sum(ticket totals)
```

`KIDS_CHAIR` receives a 50% base discount. Monetary components use `BigDecimal`, with missing values treated as zero.

## `finalizeReservationWithPayment(reservationId, method)`

### Function signature

```java
public TourReservation finalizeReservationWithPayment(Integer reservationId, PaymentMethod method)
```

### Parameters

`reservationId` is required and identifies the held booking. `method` is the selected payment method.

Access: customer, admin, or manager. The reservation is database-locked. The method validates ownership, pending status, hold expiry, and tour availability before executing payment. A completed payment confirms the reservation, books seats, approves and confirms tickets, marks them paid, clears the hold, and notifies the customer. Pending payment preserves state; failed payment returns a safe retry message.

| Code | Exact message |
|---|---|
| `RESERVATION_NOT_FOUND` | `"Reservation was not found."` |
| Default | `"You are not authorized to pay for this reservation."` |
| `RESERVATION_NOT_PAYABLE` | `"This reservation can no longer be paid because it is {status}."` |
| `RESERVATION_HOLD_EXPIRED` | `"Your reservation hold expired. Please select your seats again."` |
| `TOUR_NOT_BOOKABLE` | `"This tour is no longer available for booking."` |
| `PAYMENT_FAILED` | `"We could not complete the payment. Please try another payment method."` |

## `expirePendingReservations()`

### Function signature

```java
public void expirePendingReservations()
```

### Parameters

None.

Runs at `${booking.hold-cleanup-ms:60000}`. Expired pending reservations release inventory and seats, cancel tickets, fail pending payments, clear their hold, and notify the customer that no payment was taken. Non-pending records are ignored, making cleanup repeat-safe.

## `cancelReservation(reservationId)`

### Function signature

```java
public TourReservation cancelReservation(Integer reservationId)
```

### Parameters

`reservationId` (`Integer`, required) identifies the booking to cancel.

Validates ownership and state, calculates any refund, credits the wallet, releases capacity and seats, cancels tickets, cancels the reservation, and sends a notification.

| Notice before tour | Refund | Transaction description |
|---|---:|---|
| More than 14 days | 100% | `Full refund (> 2 weeks notice)` |
| 7 through 14 days | 50% | `50% Partial refund (1-2 weeks notice)` |
| Fewer than 7 days | 0% | `No refund (< 1 week notice). Cancellation fee applied.` |

Failures: `"Reservation not found"`, `"You are not authorized to cancel this reservation."`, `"Reservation is already cancelled."`, and `"Cannot cancel a reservation for a tour that is already completed."`

## `updateStatus(id, newStatus)`

### Function signature

```java
public TourReservation updateStatus(Integer id, GenericStatus newStatus)
```

### Parameters

`id` identifies the reservation and `newStatus` is its requested workflow state.

Access: admin, manager, or employee. Cancellation delegates to the full cancellation workflow. Other transitions pass through `DomainWorkflowValidator` before saving.

## `filter(filter)`

### Function signature

```java
public PageResponse<TourReservation> filter(ReservationFilterRequest filter)
```

### Parameters

`filter` contains status, ownership, agency, date-range, search, pagination, and sort criteria.

Customers are forcibly scoped to their own ID. Optional criteria include status, customer, agency, booking-date range, and free text over reservation number, customer name, or tour title. Sort fields are limited to `id`, `reservationNumber`, `requestedSlots`, `totalPrice`, `status`, and `bookingDate`.
