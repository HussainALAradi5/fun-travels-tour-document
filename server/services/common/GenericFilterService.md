# GenericFilterService

Source: `services/common/GenericFilterService.java`.

## Functions

### `String normalizeSearch(String search)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `PageResponse<T> executeFilter(JpaSpecificationExecutor<T> repository, Specification<T> specification, GenericFilterRequest filter, String defaultSort, Set<String> allowedSorts)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `PageResponse<T> executeFilter(JpaSpecificationExecutor<T> repository, Specification<T> specification, GenericFilterRequest filter, String defaultSort, Set<String> allowedSorts, Map<String, String> sortAliases)`

**Exceptions:** none of its own; failures come from the functions it calls.
