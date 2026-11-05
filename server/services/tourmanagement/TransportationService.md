# TransportationService

Source: `services/tourmanagement/TransportationService.java`.

Vehicles of an agency: registration, editing, seat layout, unit status, and fleet search.

## Business logic

- Lists, search, and detail are for staff: agency staff see only their agency's vehicles, admins all. Customers get 403. Search matches provider, internal code, and registration number.
- A missing vehicle is 404. Agency staff always create vehicles in their own agency; a branch must belong to that agency. Codes are unique, and a registration number is unique per provider.
- Vehicles no longer carry seat counters: seats are booked per tour, so availability is always read for a tour (`GET /api/seats/search?tourId=`).
- Seats are generated from the capacity and `seatConfig` (special chair counts; the rest are standard). Editing re-labels chair types only while no booking or running tour locks the layout.

## Functions

### `PageResponse<Transportation> getAll(Integer page, Integer size, String sortBy, String sortDir)`

**Runs in:** read-only transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `Transportation getById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Transportation not found | `ResourceNotFoundException` | 404 |

### `Transportation getVisible(Integer id)`

**Purpose:** A vehicle with its seats, for staff of its agency and administrators.

**Runs in:** read-only transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Transportation not found | `ResourceNotFoundException` | 404 |

### `Transportation create(TransportationCreateRequest request)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Transportation code already exists: | `IllegalArgumentException` | 400 |
| This registration already exists for the selected provider. | `IllegalArgumentException` | 400 |
| Agency not found | `ResourceNotFoundException` | 404 |
| Agency branch not found | `ResourceNotFoundException` | 404 |
| The selected branch does not belong to the selected agency. | `IllegalArgumentException` | 400 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Configuration exceeds capacity! | `WorkflowException` | 409 |

### `Transportation update(Integer id, TransportationUpdateRequest incomingData)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| This registration already exists for the selected provider. | `DuplicateResourceException` | 409 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Transportation not found | `ResourceNotFoundException` | 404 |
| Seat layout cannot be changed while seats are held by active tickets. | `WorkflowException` `SEAT_LAYOUT_LOCKED` | 409 |
| Seat layout cannot be changed while this transportation is assigned to an approved or active tour. | `WorkflowException` | 409 |
| Unsupported chair type: | `IllegalArgumentException` | 400 |
| Seat counts cannot be negative. | `IllegalArgumentException` | 400 |
| Configured seat counts exceed the transportation capacity of  . | `WorkflowException` | 409 |
| Configuration exceeds capacity! | `WorkflowException` | 409 |

### `Transportation updateStatus(Integer id, TransportationStatus newUnitStatus)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Cannot force a FULL unit to AVAILABLE. Seats must be freed via ticket cancellations. | `WorkflowException` | 409 |
| Transportation not found | `ResourceNotFoundException` | 404 |

### `PageResponse<Transportation> filter(TransportationFilterRequest filter)`

**Runs in:** read-only transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
