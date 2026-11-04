# TransportationService

Source: `services/tourmanagement/TransportationService.java`.

## Business logic

- Lists, search, and detail are for staff: agency staff see only their agency's vehicles, admins all. Customers get 403. Search matches provider, internal code, and registration number.
- A missing vehicle is 404. Agency staff always create vehicles in their own agency; a branch must belong to that agency. Codes are unique, and a registration number is unique per provider.
- Seats are generated from the capacity and `seatConfig` (special chair counts; the rest are standard). Editing re-labels chair types only while no booking or running tour locks the layout.

## Functions

### `PageResponse<Transportation> getAll(Integer page, Integer size, String sortBy, String sortDir)`

**Runs in:** read-only transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

### `Transportation getById(Integer id)`

**Runs in:** read-only transaction

### `Transportation getVisible(Integer id)`

**Purpose:** A vehicle with its seats, for staff of its agency and administrators.

**Runs in:** read-only transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

### `Transportation create(TransportationCreateRequest request)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `ImportResult importExcel(InputStream input)`

### `Transportation update(Integer id, TransportationUpdateRequest incomingData)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `Transportation updateStatus(Integer id, TransportationStatus newUnitStatus)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `PageResponse<Transportation> filter(TransportationFilterRequest filter)`

**Runs in:** read-only transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER
