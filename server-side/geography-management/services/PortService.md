# Port Service

**Source:** `src/main/java/com/server/server/services/PortService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions |
|---|---|---|---|---|---|
| `public List<Port> getAllActivePorts()` | None | Queries `ACTIVE` ports. | Selectors hide inactive ports. | Active ports; read-only. | None directly. |
| `public Port getById(Integer id)` | Required ID | Queries by ID. | Shared port resolver. | Port; read-only. | `"Port not found"`. |
| `public Port createPort(Port port)` | Port aggregate | Forces `ACTIVE` and saves. | New ports become usable immediately. | Created port. | Repository/validation failures may propagate. |
| `public Port updateStatus(Integer id, GenericStatus status)` | ID and target status | Loads, sets status, saves. | Deactivation preserves history. | Updated port. | Missing-port failure propagates. |
