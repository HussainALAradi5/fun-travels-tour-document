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
