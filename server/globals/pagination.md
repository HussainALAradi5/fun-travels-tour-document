# Pagination and sorting

`PaginationUtils.pageable` is the single page builder.

- `page` (0-based, negative becomes 0) and `size` (default 20, capped at 100).
- `sortBy` must be in the endpoint's allow-list (unknown fields return 400); `sortDir` is `asc` or `desc` (default `desc`). Aliases map friendly names to paths (`startDate` -> `tour.startDate`).
- Filters extend `GenericFilterRequest` (`page`, `size`, `search`, `sortBy`, `sortDir`) and are applied in the database query.
- Responses use `PageResponse`: `content`, `page`, `size`, `totalElements`, `totalPages`.
