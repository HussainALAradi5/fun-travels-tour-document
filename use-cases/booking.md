# Booking use cases

## UC-BK-01 Customer books a tour

- **Actor:** Customer (web or mobile).
- **Preconditions:** Signed in; tour is ACTIVE with free places; no overlapping active booking.
- **Main flow:** Customer chooses travelers, optional seats (free seats for this tour) and offered meals -> `POST /api/v1/reservations` -> server issues one ticket per traveler, assigns free seats where none was chosen, prices each ticket from stored records, lowers available places -> reservation PENDING with a 15-minute hold.
- **Failure flows:** Seat taken or under maintenance -> 409 `SEAT_NOT_AVAILABLE`; not enough places -> 409 `INSUFFICIENT_CAPACITY`; meal inactive, not offered, or duplicated -> 409; overlapping dates -> 409 `DATE_CONFLICT`.
- **Result:** Places and seats are held for this tour only; the same seats stay free on the vehicle's other tours.

## UC-BK-02 Customer pays with wallet

- **Preconditions:** Reservation PENDING, hold not expired, tour ACTIVE and not started.
- **Main flow:** `POST /api/v1/payments/execute/{id}?method=WALLET` -> wallet debited by the server total -> reservation CONFIRMED, tickets CONFIRMED, APPROVED, paid; QR codes shown.
- **Failure flows:** Balance too low -> 409 `INSUFFICIENT_BALANCE` (nothing changes, hold stays); hold expired -> reservation cancelled, 409 `RESERVATION_HOLD_EXPIRED`.
- **Result:** Wallet transaction `PAYMENT` recorded; customer notified.

## UC-BK-03 Customer cancels one ticket

- **Main flow:** `PUT /api/v1/tickets/{id}/cancel` -> paid ticket refunded by notice period (more than 14 days 100%, 7-14 days 50%, under 7 days 0%) as `PARTIAL_REFUND` -> one place released, seat free for this tour -> pending reservation total reduced; reservation cancelled if no ticket remains.
- **Failure flows:** Another customer's ticket -> 403; already cancelled or completed -> 409.

## UC-BK-04 Customer cancels a reservation

- **Main flow:** `PATCH /api/v1/reservations/{id}/cancel` -> for a paid reservation, refund = notice-period share of the **remaining active** tickets -> places released -> reservation CANCELLED.
- **Failure flows:** Already cancelled -> 409 `ALREADY_CANCELLED`; rejected or completed -> 409; tour completed -> 409.
- **Result:** No ticket is ever refunded twice.

## UC-BK-05 Hold expires

- **Actor:** System (every 60 s).
- **Main flow:** PENDING reservations past `holdExpiresAt` -> tickets cancelled, places released, pending payments FAILED -> customer notified "No payment was taken".
