# Generic Filter Service

**Source:** `src/main/java/com/server/server/services/filter/GenericFilterService.java`

## Function reference

| Function | Signature | Parameters | Function logic | Business logic | Return value | Exceptions |
|---|---|---|---|---|---|---|
| `normalizeSearch` | `protected String normalizeSearch(String search)` | Optional text | Trims, lowercases, and surrounds nonblank text with `%`; returns `null` for blank input. | Gives all specifications consistent case-insensitive contains matching. | Normalized SQL-like pattern or `null`. | None directly. |
| `executeFilter` | `protected PageResponse<T> executeFilter(JpaSpecificationExecutor<T> repository, Specification<T> specification, GenericFilterRequest filter, String defaultSort, Set<String> allowedSorts)` | Repository, specification, filter, default sort, allow-list | Delegates to the alias-aware overload with an empty alias map. | Prevents repeated pagination code. | `PageResponse<T>`. | Propagates repository and pagination validation errors. |
| `executeFilter` | `protected PageResponse<T> executeFilter(..., Map<String,String> sortAliases)` | Same inputs plus public-to-entity sort aliases | Builds a safe pageable, executes the specification, and maps the Spring page. | Enforces bounded pages and safe sort fields across domains. | `PageResponse<T>`. | Propagates repository and pagination validation errors. |

This abstract service is invoked inside each concrete service's read-only transaction.
