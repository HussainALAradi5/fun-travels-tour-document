# Port Service

**Source:** `src/main/java/com/server/server/services/PortService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions |
|---|---|---|---|---|---|
| `public List<Port> getAllActivePorts()` | None | Queries `ACTIVE` ports. | Selectors hide inactive ports. | Active ports; read-only. | None directly. |
| `public Port getById(Integer id)` | Required ID | Queries by ID. | Shared port resolver. | Port; read-only. | `"Port not found"`. |
| `public Port createPort(Port port)` | Port aggregate | Forces `ACTIVE` and saves. | New ports become usable immediately. | Created port. | Repository/validation failures may propagate. |
| `public Port updateStatus(Integer id, GenericStatus status)` | ID and target status | Loads, sets status, saves. | Deactivation preserves history. | Updated port. | Missing-port failure propagates. |

## Expected behavior and displayed errors

### `getAllActivePorts()`

Returns only `ACTIVE` ports for operational selectors. Inactive records remain stored for historical references but are not offered for new work. Unexpected storage failures use the generic safe API error.

### `getById(Integer id)`

Returns the requested port as a managed domain record. If no record exists, the displayed message is `Port not found`.

### `createPort(Port port)`

Forces the new port to `ACTIVE`, persists it, and returns the saved record with its ID. The client cannot create an already-disabled port through this command. Bean-validation errors should identify the invalid field; database details must not be exposed.

### `updateStatus(Integer id, GenericStatus status)`

Loads the port, changes only its lifecycle status, and saves it. This is a soft operational change and preserves references from existing tours. A missing port displays `Port not found`; an invalid status value displays a clear `status` field error.
