# PortService

Source: `services/geography/PortService.java`.

## Functions

### `List<Port> getAllActivePorts()`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `Port getById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Port not found | `ResourceNotFoundException` | 404 |

### `Port createPort(PortCreateRequest request)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country not found | `ResourceNotFoundException` | 404 |
| City not found | `ResourceNotFoundException` | 404 |
| The selected city does not belong to the selected country. | `IllegalArgumentException` | 400 |

### `Port updateStatus(Integer id, GenericStatus status)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Port not found | `ResourceNotFoundException` | 404 |
