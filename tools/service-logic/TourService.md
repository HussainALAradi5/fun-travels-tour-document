## Business logic

### Visibility

`getVisible` (the public `GET /api/tours/{id}`): ACTIVE (bookable) tours are public; other tours are shown to administrators, the owning agency's staff, and customers holding a ticket for the tour. Anyone else gets 404, so pending or cancelled tours do not leak. `getAll` and `filter` list every tour for administrators, the agency's tours for agency staff, and only ACTIVE tours for everyone else. The tour price is `basePrice` minus `discountPrice` (`totalPrice`); the old duplicate `price` column was removed.

### `create(TourCreateRequest request)`

Agency staff create tours for their own agency (and branch). Cities must belong to their countries, start date cannot be in the past, capacity cannot exceed the vehicle capacity, the vehicle cannot serve an overlapping tour, and offered meals must be ACTIVE and belong to the tour's agency (or be shared). New tours start PENDING.

### `updateTour(Integer id, Tour incomingData)` / `updateStatus(Integer id, GenericStatus newStatus)`

Who may manage a tour: admins always; owners for their agency; managers for their branch or branch-less tours of their agency; employees only tours they created. Capacity cannot drop below sold/held places. The vehicle cannot change once tickets exist (`TRANSPORTATION_LOCKED`).

Status workflow: PENDING -> APPROVED or CANCELLED; APPROVED -> ACTIVE or CANCELLED; ACTIVE -> COMPLETED or CANCELLED; CANCELLED -> PENDING. Cancellation requires at least 14 days to departure and no more than one third of capacity booked; every active booking is then cancelled and paid tickets are fully refunded.

### `autoProcessScheduledTours()`

Nightly: PENDING tours past their start date are cancelled; ACTIVE/APPROVED tours past their end date are completed, their tickets completed, and each traveler greeted once.
