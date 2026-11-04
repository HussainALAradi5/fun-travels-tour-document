# TransportationService

Source: `services/tourmanagement/TransportationService.java`.

## Functions

### `PageResponse<Transportation> getAll(Integer page, Integer size, String sortBy, String sortDir)`

**Runs in:** read-only transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

### `Transportation getById(Integer id)`

**Runs in:** read-only transaction

### `Transportation create(TransportationCreateRequest request)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `ImportResult importExcel(InputStream input)`

### `Transportation update(Integer id, TransportationUpdateRequest incomingData)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `Transportation updateStatus(Integer id, TransportationStatus newUnitStatus)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `PageResponse<Transportation> filter(TransportationFilterRequest filter)`

**Runs in:** read-only transaction
