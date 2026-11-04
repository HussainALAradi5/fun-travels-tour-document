# GenericFilterService

Source: `services/common/GenericFilterService.java`.

## Functions

### `String normalizeSearch(String search)`

### `PageResponse<T> executeFilter(JpaSpecificationExecutor<T> repository, Specification<T> specification, GenericFilterRequest filter, String defaultSort, Set<String> allowedSorts)`

### `PageResponse<T> executeFilter(JpaSpecificationExecutor<T> repository, Specification<T> specification, GenericFilterRequest filter, String defaultSort, Set<String> allowedSorts, Map<String, String> sortAliases)`
