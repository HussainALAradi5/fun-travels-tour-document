# Booking use cases

## UC-BK-01 Customer books a tour

- **Actor:** Customer (web or mobile).
- **Preconditions:** Signed in; tour is ACTIVE with free places; no overlapping active booking.
- **Main flow:** Customer sets the group in one step (adults and children steppers, any number up to the places left), optionally taps "Seat my group together" (children get kids chairs while free, adults standard seats, side by side), picks offered meals per traveler or copies one traveler's meals to everyone, and sees a live price with the agency's kids discount and the tour's sale price -> `POST /api/reservations` with one ticket selection per traveler -> server issues one ticket per traveler, gives **standard** seats to travelers without a chosen seat, prices each ticket from stored records (see [pricing](../server/globals/pricing-and-refunds.md)), lowers available places -> reservation PENDING with a 15-minute hold.
- **Failure flows:** Seat taken or under maintenance -> 409 `SEAT_NOT_AVAILABLE`; the same seat twice -> 409 `DUPLICATE_SEAT`; no standard seat left for a traveler without a chosen seat -> 409 `SEAT_CHOICE_REQUIRED`; not enough places -> 409 `INSUFFICIENT_CAPACITY`; meal inactive, not offered, or duplicated -> 409; overlapping dates -> 409 `DATE_CONFLICT`.
- **Result:** Places and seats are held for this tour only; the same seats stay free on the vehicle's other tours.

## UC-BK-02 Customer pays with wallet

- **Preconditions:** Reservation PENDING, hold not expired, tour ACTIVE and not started.
- **Main flow:** `POST /api/payments/execute/{id}?method=WALLET` -> wallet debited by the server total -> reservation CONFIRMED, tickets CONFIRMED, APPROVED, paid; QR codes shown.
- **Failure flows:** Balance too low -> 409 `INSUFFICIENT_BALANCE` (nothing changes, hold stays); hold expired -> reservation cancelled, 409 `RESERVATION_HOLD_EXPIRED`.
- **Result:** Wallet transaction `PAYMENT` recorded; customer notified.

## UC-BK-03 Customer cancels one ticket

- **Main flow:** Customer opens Cancel -> the app loads `GET /api/tickets/{id}/refund-quote` and shows "Cancel now and $X of $Y (P%) returns to your wallet; the tour starts in N days" -> customer confirms -> `PUT /api/tickets/{id}/cancel` -> paid ticket refunded by the **tour agency's policy** (default: more than 14 days 100%, 7-14 days 50%, under 7 days 0%) as `PARTIAL_REFUND` -> one place released, seat free for this tour -> pending reservation total reduced; reservation cancelled if no ticket remains.
- **Failure flows:** Another customer's ticket -> 403; already cancelled or completed -> 409.

## UC-BK-04 Customer cancels a reservation

- **Main flow:** the app shows `GET /api/reservations/{id}/refund-quote` first -> `PATCH /api/reservations/{id}/cancel` -> for a paid reservation, refund = the agency policy's share of the **remaining active** tickets (always equal to the quote) -> places released -> reservation CANCELLED.
- **Failure flows:** Already cancelled -> 409 `ALREADY_CANCELLED`; rejected or completed -> 409; tour completed -> 409.
- **Result:** No ticket is ever refunded twice.

## UC-BK-05 Hold expires

- **Actor:** System (every 60 s).
- **Main flow:** PENDING reservations past `holdExpiresAt` -> tickets cancelled, places released, pending payments FAILED -> customer notified "No payment was taken".

## UC-BK-06 Owner sets the agency's discount and refund rules

- **Actor:** Agency owner (or an administrator for any agency).
- **Preconditions:** Signed in as the agency's owner.
- **Main flow:** Agency page -> Pricing and refunds tab -> owner sets the kids chair discount (%), the full-refund limit (days), the partial-refund start (days) and percentage; the preview shows the customer timeline -> `PUT /api/agencies/{id}/policy` -> new bookings and cancellations use the rules; already paid tickets keep their price.
- **Failure flows:** Manager, employee or customer -> 403; percent outside 0-100 or days outside 0-365 -> 400 with field errors; partial window starting after the full window -> 400.
- **Result:** `GET /api/agencies/{id}/policy` and every tour response (`policy`) show the rules with a one-line summary.

## UC-BK-07 Agency puts a tour on sale

- **Actor:** Owner, manager or administrator.
- **Main flow:** Tour create or edit -> Sale Discount -> `discountPrice` is taken off the base price for every traveler; the kids discount applies to the sale price.
- **Failure flows:** Discount above the base price -> 409 `DISCOUNT_ABOVE_PRICE`; negative -> 400.
