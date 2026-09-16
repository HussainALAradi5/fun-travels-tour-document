# Generic Filter Service

**Source:** `src/main/java/com/server/server/services/filter/GenericFilterService.java`

## Function reference

| Function | Signature | Parameters | Function logic | Business logic | Return value | Exceptions |
|---|---|---|---|---|---|---|
| `normalizeSearch` | `protected String normalizeSearch(String search)` | Optional text | Trims, lowercases, and surrounds nonblank text with `%`; returns `null` for blank input. | Gives all specifications consistent case-insensitive contains matching. | Normalized SQL-like pattern or `null`. | None directly. |
| `executeFilter` | `protected PageResponse<T> executeFilter(JpaSpecificationExecutor<T> repository, Specification<T> specification, GenericFilterRequest filter, String defaultSort, Set<String> allowedSorts)` | Repository, specification, filter, default sort, allow-list | Delegates to the alias-aware overload with an empty alias map. | Prevents repeated pagination code. | `PageResponse<T>`. | Propagates repository and pagination validation errors. |
| `executeFilter` | `protected PageResponse<T> executeFilter(..., Map<String,String> sortAliases)` | Same inputs plus public-to-entity sort aliases | Builds a safe pageable, executes the specification, and maps the Spring page. | Enforces bounded pages and safe sort fields across domains. | `PageResponse<T>`. | Propagates repository and pagination validation errors. |

This abstract service is invoked inside each concrete service's read-only transaction.

## Expected behavior and displayed errors

### `normalizeSearch(String search)`

Null, empty, and whitespace-only input returns `null`, meaning “do not apply a text predicate.” Otherwise, the value is trimmed, lowercased, and wrapped for a contains match. This keeps search behavior identical across services and avoids treating an empty search box as zero results. The helper has no direct user-visible error.

### `executeFilter(...)`

The basic overload delegates to the alias-aware overload. The final overload validates pagination and sorting, resolves public sort aliases to safe entity properties, executes the supplied JPA specification, and maps metadata and content into the shared `PageResponse<T>`.

Only allow-listed sort properties may reach JPA. Invalid page, size, direction, or sort values display the shared validation message. Repository or specification failures must be logged and returned as a generic safe request failure; generated SQL and entity internals must not be exposed.
