# Seat Service

**Source:** `src/main/java/com/server/server/services/tourmanagement/SeatService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions / authorization |
|---|---|---|---|---|---|
| `public PageResponse<Seat> getAll(Integer page, Integer size, String sortDir)` | Optional pagination/direction | Builds a seat-code pageable and queries one page. | Prevents unbounded inventory responses. | Seat page; read-only. | Pagination validation may propagate. |
| `public Seat getById(Integer id)` | Required seat ID | Null-checks and queries by ID. | Resolves a managed seat before price/status logic. | Seat; read-only. | `"Seat not found"`; null `"id must not be null"`. |
| `public Seat updateSeat(Integer id, Seat updatedData)` | ID and optional chair type/status/modifier fields | Loads seat, checks booking and tour locks, copies supplied fields, saves. | Booked seats and layouts attached to approved tours cannot be reclassified. | Updated seat. | `"Cannot change the chair type of a booked seat."`; `"Seat layout is locked. The vehicle is assigned to an APPROVED tour."` Roles: owner, manager, admin. |
| `public PageResponse<Seat> filter(SeatFilterRequest filter)` | Unit, status, chair type, search, pagination/sort | Builds combined specifications and queries one page. | Supports scalable seat management and server-side search. | Filtered page; read-only. | Pagination/repository failures may propagate. |
| `public Seat updateStatus(Integer id, SeatStatus status)` | Required ID and target status | Loads, sets status, saves. | Operational staff can remove or return seats to service. | Updated seat. | Missing-seat failure propagates. |
| `public List<Seat> filter(Integer transportId, SeatStatus status, ChairType chairType)` | Optional criteria | Combines predicates and returns matches. | Internal non-paged lookup for constrained inventory workflows. | Matching seats; read-only. | None directly. |
| `private Specification<Seat> hasTransportId/hasStatus/hasChairType(...)` | Optional criterion | Returns conjunction when absent or equality predicate when present. | Keeps filters composable. | JPA specification; no side effects. | None directly. |

## Detailed behavior and displayed errors

### `getAll(Integer page, Integer size, String sortDir)`

- **What should happen:** Return one validated page of seats ordered by seat code in the requested direction.
- **Business rule:** Seat administration never returns an unbounded inventory result.
- **Displayed errors:** Invalid page, size, or direction displays the shared pagination/sort validation message.

### `getById(Integer id)`

- **What should happen:** Return the complete managed seat required by configuration workflows.
- **Displayed errors:** A null ID displays `id must not be null`; an unknown ID displays `Seat not found`.

### `updateSeat(Integer id, Seat updatedData)`

- **What should happen:** Apply permitted seat classification and operational changes while preserving its transportation ownership and protected identity.
- **Processing:** Load the managed seat, determine whether chair type is actually changing, reject protected changes, copy permitted non-null fields, and save in one transaction.
- **Business rules:** A booked seat cannot change chair type. A transportation layout assigned to an approved tour is locked. These rules preserve existing prices, reservations, and manifests.
- **Displayed errors:** A booked-seat reclassification displays `Cannot change the chair type of a booked seat.` A locked layout displays `Seat layout is locked. The vehicle is assigned to an APPROVED tour.` An unknown seat displays `Seat not found`.

### `filter(SeatFilterRequest filter)`

- **What should happen:** Return the requested page after combining transportation, status, chair type, and free-text predicates.
- **Business rule:** Search and filtering execute in the database rather than loading all seats in the client.
- **Displayed errors:** Invalid paging or sorting displays the shared validation message; unexpected repository failures use the safe generic API error.

### `updateStatus(Integer id, SeatStatus status)`

- **What should happen:** Set the operational state of an existing seat and return the saved record.
- **Business rule:** Status changes remove or return a seat to service without deleting its history.
- **Displayed errors:** An unknown ID displays `Seat not found`. Invalid or missing enum input displays a clear field-validation message for `status`.

### `filter(Integer transportId, SeatStatus status, ChairType chairType)` and predicate helpers

- **What should happen:** Return internal matches using only the criteria that were supplied; absent criteria behave as no restriction.
- **Displayed errors:** These internal helpers raise no intentional user-facing business error. Repository failures are handled at the calling API boundary.
