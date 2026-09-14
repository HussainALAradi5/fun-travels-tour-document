# Implementation Updates

This document records the cross-cutting improvements reflected in the current server and client applications.

## API consistency

Collection endpoints use the shared `PageResponse<T>` contract:

```json
{
  "content": [],
  "page": 0,
  "size": 20,
  "totalElements": 0,
  "totalPages": 0
}
```

`PaginationUtils` normalizes page size, validates sort fields, supports `asc` and `desc`, and caps requests at 100 records. Filter DTOs expose domain-specific search, status, date-range, agency, and branch parameters. API failures use a stable envelope containing `success`, `code`, `message`, `data`, `fieldErrors`, `timestamp`, and `path`.

## Agency-backed selectors

Agency and branch selectors do not download an unlimited list to the browser. The reusable client selector requests paginated results from the server, searches after a 300 ms debounce, loads the first page for an empty query, supports additional pages, and permits deselection. Changing an agency clears an incompatible branch selection.

## Transportation and seats

- Transportation creation accepts explicit `agencyId`, optional `branchId`, and a nested `seatConfig`.
- Agency/branch ownership is validated on the server.
- The selected seat counts generate that number of physical `Seat` records; remaining capacity becomes `STANDARD` seating.
- Existing layouts support one-operation bulk reclassification when no protected seats or tours make the layout unsafe to change.
- List responses omit the lazy seat collection; detail responses fetch seats, agency, and branch explicitly. This prevents `LazyInitializationException` and N+1 list queries.
- Excel import is processed by the backend, not the browser, and reports successful and failed rows independently.

## Client architecture

- `PaginatedSearchSelect` composes Chakra UI combobox primitives around the shared `PageResponse<SelectOption>` contract.
- `DynamicForm` supports nested object paths and memoized fields, preventing expensive whole-form rerenders while typing.
- `GuidedStepsDialog` supplies reusable customer instructions on tour and ticket pages.
- The date picker supports range selection, light/dark modes, deterministic server rendering, accessible controls, and valid HTML nesting.
- Hydration-sensitive clock/browser behavior is deferred through `useIsHydrated`; notification listeners are registered and cleaned up through React effects.
- Network failures are converted to user-facing messages and handled by state-loading hooks without unhandled promise rejections.

## Configuration and repository hygiene

Runtime secrets belong in the ignored `application.properties` file or environment variables. `application.properties.example` documents required keys without real credentials. Maven repositories, logs, runtime uploads, and API-tool environment exports are excluded from source control.

