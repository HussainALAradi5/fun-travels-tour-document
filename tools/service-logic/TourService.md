## Business logic

### `create(TourCreateRequest request)`

Agency staff create tours for their own agency (and branch, when they have one). Cities must belong to their countries, start date cannot be in the past, capacity cannot exceed the vehicle capacity, the vehicle cannot serve an overlapping tour, and offered meals must be ACTIVE and belong to the tour's agency (or be shared). New tours start PENDING. The price is `basePrice` minus `discountPrice` (`totalPrice`).

### `updateTour(Integer id, TourUpdateRequest request)`

Who may manage a tour (`requireCanManage`, also used by the status workflow): admins always; owners for their agency; managers for their branch or branch-less tours of their agency; employees only tours they created. Capacity cannot drop below sold/held places. The vehicle cannot change once tickets exist (`TRANSPORTATION_LOCKED`).

Reading tours is in `TourCatalogService`, the status workflow in `TourStatusService`, and nightly housekeeping in `TourSchedulerService`.
