# Tour and inventory use cases

## UC-TR-01 Owner publishes a tour

- **Preconditions:** Owner signed in; vehicle of the agency free on those dates; meals active and of the agency.
- **Main flow:** `POST /api/tours` (PENDING) -> `PUT /api/tours/{id}/status?status=APPROVED` -> `...status=ACTIVE` (places reset to capacity) -> tour appears in the public catalog.
- **Failure flows:** Start date in the past, capacity above the vehicle's, vehicle on an overlapping tour, meal inactive or of another agency -> 409; owner of another agency -> 403.

## UC-TR-02 Agency cancels a tour

- **Preconditions:** At least 14 days before departure; at most one third of capacity booked.
- **Main flow:** `status=CANCELLED` -> every active reservation cancelled, paid tickets refunded in full, places released, customers notified.
- **Failure flows:** Too close to departure or too many bookings -> 409.

## UC-SE-01 Staff puts a seat into maintenance

- **Main flow:** `PATCH /api/seats/{id}/status?status=MAINTENANCE` -> seat is never sold on any tour until set back to AVAILABLE.
- **Failure flows:** Seat held by an active ticket -> 409 `SEAT_IN_USE`; setting RESERVED or BOOKED manually -> 409 `SEAT_STATUS_LOCKED`; changing chair type or price while the vehicle is on an approved or active tour -> 409 `SEAT_LAYOUT_LOCKED`.
