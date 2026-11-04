## Business logic

- `search` with `tourId` returns the tour's vehicle seats and reports seats taken on that tour as `BOOKED`; without it, the stored physical status is returned.
- Staff may only set `AVAILABLE` or `MAINTENANCE`; `RESERVED`/`BOOKED` come from tickets (`SEAT_STATUS_LOCKED`). A seat held by an active ticket cannot go to maintenance (`SEAT_IN_USE`).
- Chair type and price modifier are locked while the seat is held by an active ticket or the vehicle is assigned to an APPROVED or ACTIVE tour (`SEAT_LAYOUT_LOCKED`).
- Agency staff can only edit seats of their agency's vehicles.
