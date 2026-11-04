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

Locks the reservation, checks ownership (customer) or agency (staff), requires PENDING status, an unexpired hold, and an ACTIVE tour that has not started. Wallet payments debit the wallet and confirm immediately: active tickets become CONFIRMED, APPROVED, and paid. Card and PayPal payments stay PENDING until a verified provider webhook completes them (not implemented; listed under known limitations in the security review).

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
