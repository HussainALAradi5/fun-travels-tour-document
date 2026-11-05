# TourCatalogService

Source: `services/tourmanagement/TourCatalogService.java`.

Read side of tours: the public catalog, lists and search, and who may see which tour.

## Business logic

`getVisible` (the public `GET /api/tours/{id}`): ACTIVE (bookable) tours are public; other tours are shown to administrators, the owning agency's staff, and customers holding a ticket for the tour. Anyone else gets 404, so pending or cancelled tours do not leak.

`getAll` and `filter` list every tour for administrators, the agency's tours for agency staff (managers and employees also only their branch's), and only ACTIVE tours for everyone else. `getCatalogTours` is the public catalog: bookable tours by start/end country and date range.

## Functions

### `PageResponse<Tour> getAll(Integer page, Integer size, String sortBy, String sortDir)`

**Purpose:** Admins and agency staff list every tour (staff within their agency); everyone else only bookable ones.

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `Tour getVisible(Integer id)`

**Purpose:** One tour by id for the public endpoint. Bookable (ACTIVE) tours are public; others are shown to administrators, the owning agency's staff, and customers holding a ticket for it. Anyone else gets 404, so pending or cancelled tours do not leak.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Tour not found | `ResourceNotFoundException` | 404 |

### `PageResponse<Tour> getCatalogTours(Integer startCountryId, Integer endCountryId, LocalDate start, LocalDate end, Integer page, Integer size)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `PageResponse<Tour> filter(TourFilterRequest filter)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.
