# PortService

Source: `services/geography/PortService.java`.

## Functions

### `List<Port> getAllActivePorts()`

**Runs in:** read-only transaction

### `Port getById(Integer id)`

**Runs in:** read-only transaction

### `Port createPort(PortCreateRequest request)`

**Runs in:** transaction

### `Port updateStatus(Integer id, GenericStatus status)`

**Runs in:** transaction
