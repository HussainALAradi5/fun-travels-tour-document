# TourReservationService

Source: `services/tourmanagement/TourReservationService.java`.

## Business logic

### `create(ReservationCreateRequest request)`

1. Customers always book for themselves; staff must pass an active `user`. Agency staff may only book tours of their own agency.
2. Rejects a booking whose dates overlap another PENDING, APPROVED, or CONFIRMED reservation of the same customer.
3. Builds one ticket per traveler. When `tickets` is empty, `requestedSlots` blank tickets are issued (default 1), so a booking is never priced at zero.
4. Holds places and seats through `InventoryService.reserve` (tour row locked), then prices every ticket from stored tour, seat, and meal records. The reservation total is the sum of its tickets.
5. Saves the reservation as PENDING with a 15-minute hold (`BookingRules.HOLD_MINUTES`) and notifies the customer.

| Case | Result |
| --- | --- |
| Client sends `totalPrice` | Ignored; price is calculated server-side |
| Tour not ACTIVE | 409 `TOUR_NOT_BOOKABLE` |
| Not enough places | 409 `INSUFFICIENT_CAPACITY` |
| Seat taken on this tour, under maintenance, or on another vehicle | 409 `SEAT_NOT_AVAILABLE` / `INVALID_SEAT_FOR_TOUR` |
| Meal not offered by the tour, inactive, or chosen twice | 409 `MEAL_NOT_OFFERED` / `MEAL_INACTIVE` / `DUPLICATE_MEAL` |
| Date overlap with another booking | 409 `DATE_CONFLICT` |

### `finalizeReservationWithPayment(Integer reservationId, PaymentMethod method)`

Locks the reservation, checks ownership (customer) or agency (staff), requires PENDING status, an unexpired hold, and an ACTIVE tour that has not started. The wallet is debited and the reservation confirmed at once: active tickets become CONFIRMED, APPROVED, and paid. Other payment methods are rejected with `PAYMENT_METHOD_UNSUPPORTED` (see PaymentService).

| Case | Result |
| --- | --- |
| Wallet balance too low | 409 `INSUFFICIENT_BALANCE`, nothing changes |
| Hold expired | Reservation expires, places released, 409 `RESERVATION_HOLD_EXPIRED` |
| Already confirmed or cancelled | 409 `RESERVATION_NOT_PAYABLE` |

### `cancelReservation(Integer reservationId)`

Rejects a second cancellation (`ALREADY_CANCELLED`) and cancellation of REJECTED or COMPLETED reservations. For a CONFIRMED reservation, the refund is the notice-period share of the **still-active** tickets only: more than 14 days before departure 100%, 7 to 14 days 50%, under 7 days 0%. Tickets cancelled earlier were already refunded and are not refunded again. Only active tickets release places; their seats become free for that tour.

### `updateStatus(Integer id, GenericStatus newStatus)`

Staff may REJECT a pending reservation (places released) or COMPLETE a confirmed one. CONFIRMED is reachable only through payment; CANCELLED delegates to `cancelReservation`.

### `syncAfterTicketCancellation(TourReservation reservation)`

After a single ticket is cancelled: a reservation with no active tickets becomes CANCELLED; a PENDING reservation gets its slot count and total reduced so the customer never pays for a cancelled traveler.

### `expirePendingReservations()`

Every `booking.hold-cleanup-ms` (default 60 s), expires PENDING reservations whose hold passed: active tickets cancelled, places released, pending payments marked FAILED, customer notified.

## Functions

### `PageResponse<TourReservation> getAll(Integer page, Integer size, String sortDir)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `TourReservation getById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Reservation not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `RefundQuoteResponse refundQuote(Integer id)`

**Purpose:** What cancelling the whole booking now would refund; nothing for an unpaid or cancelled booking.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Reservation not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `TourReservation create(ReservationCreateRequest request)`

**Purpose:** Holds places and seats for `BookingRules#HOLD_MINUTES` minutes while payment is pending. Every traveler receives a ticket priced from stored records.

**Runs in:** transaction; roles: CUSTOMER, EMPLOYEE, ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| You already have an active reservation that conflicts with these dates. | `WorkflowException` `DATE_CONFLICT` | 409 |
| A reservation customer is required. | `WorkflowException` `CUSTOMER_REQUIRED` | 409 |
| User not found | `ResourceNotFoundException` | 404 |

### `TourReservation finalizeReservationWithPayment(Integer reservationId, PaymentMethod method)`

**Runs in:** transaction; roles: CUSTOMER, ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Reservation was not found. | `WorkflowException` `RESERVATION_NOT_FOUND` | 409 |
| This reservation can no longer be paid because it is  . | `WorkflowException` `RESERVATION_NOT_PAYABLE` | 409 |
| Your reservation hold expired. Please select your seats again. | `WorkflowException` `RESERVATION_HOLD_EXPIRED` | 409 |
| This tour is no longer available for booking. | `WorkflowException` `TOUR_NOT_BOOKABLE` | 409 |
| We could not complete the payment. Please try another payment method. | `WorkflowException` `PAYMENT_FAILED` | 409 |
| Status change not allowed by the workflow | `WorkflowException` | 409 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `void expirePendingReservations()`

**Runs in:** transaction; scheduled `fixedDelayString = "${booking.hold-cleanup-ms:60000}"`

**Exceptions:** none of its own; failures come from the functions it calls.

### `TourReservation cancelReservation(Integer reservationId)`

**Purpose:** Customer or staff cancellation. Paid reservations are refunded by the notice-period policy.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Reservation is already cancelled. | `WorkflowException` `ALREADY_CANCELLED` | 409 |
| Cannot cancel a reservation for a tour that is already completed. | `WorkflowException` | 409 |
| Status change not allowed by the workflow | `WorkflowException` | 409 |
| Reservation not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `TourReservation updateStatus(Integer id, GenericStatus newStatus)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Status change not allowed by the workflow | `WorkflowException` | 409 |
| Reservation not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Reservation is already cancelled. | `WorkflowException` `ALREADY_CANCELLED` | 409 |
| Cannot cancel a reservation for a tour that is already completed. | `WorkflowException` | 409 |

### `void syncAfterTicketCancellation(TourReservation reservation)`

**Purpose:** Recalculates slots and total after one ticket of a reservation is cancelled.

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `PageResponse<TourReservation> filter(ReservationFilterRequest filter)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
