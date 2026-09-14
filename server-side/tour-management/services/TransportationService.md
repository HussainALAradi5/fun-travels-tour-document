# Transportation Service

**Source:** `src/main/java/com/server/server/services/tourmanagement/TransportationService.java`

This service manages transport inventory, agency ownership, generated seat layouts, filtering, lifecycle status, and bulk spreadsheet import.

## `getAll(page, size, sortBy, sortDir)`

### Function signature

```java
public PageResponse<Transportation> getAll(Integer page, Integer size, String sortBy, String sortDir)
```

### Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `page` | `Integer` | No | Zero-based page index. |
| `size` | `Integer` | No | Requested page size. |
| `sortBy` | `String` | No | Allow-listed transportation property. |
| `sortDir` | `String` | No | `asc` or `desc`. |

Returns `PageResponse<Transportation>`. `PaginationUtils` applies defaults and accepts only `id`, `transportationNumber`, `code`, `providerName`, `type`, and `unitStatus`. Access requires admin, manager, employee, or owner authority.

### Function logic and business logic

Normalizes pagination, validates the requested sort field, queries one repository page, and preserves bounded API responses. No explicit exception is raised directly; pagination validation errors may propagate. The method is read-only and has no side effects.

## `getById(id)`

### Function signature

```java
public Transportation getById(Integer id)
```

### Parameters

`id` (`Integer`, required) identifies the transportation unit.

Loads one unit with seats using `findWithSeatsById`, keeping detail mapping independent of lazy Hibernate proxies.

Failure: `IllegalArgumentException` with `"Transportation unit not found."`

## `create(request)`

### Function signature

```java
public Transportation create(TransportationCreateRequest request)
```

### Parameters

`request` is required and contains registration, code, type, provider, capacity, agency ID, optional branch ID, and optional seat configuration.

Access requires admin, manager, or owner authority.

Logic:

1. Resolve `agencyId` and optional `branchId` to managed entities.
2. Verify that the branch belongs to the selected agency.
3. Trim textual identifiers and map capacity, type, provider, ownership, and seat configuration.
4. Reject duplicate code or provider/registration pairs.
5. Initialize status to `ACTIVE`, unit status to `AVAILABLE`, and remaining seats to total capacity.
6. Generate the complete seat layout when seats were not supplied; otherwise attach supplied seats to the unit.
7. Save the aggregate in one transaction.

Failures:

| Type | Exact message | Condition |
|---|---|---|
| `ResourceNotFoundException` | Resource-standard agency message | `agencyId` does not exist. |
| `ResourceNotFoundException` | Resource-standard agency-branch message | `branchId` does not exist. |
| `IllegalArgumentException` | `"The selected branch does not belong to the selected agency."` | Ownership mismatch. |
| `IllegalArgumentException` | `"Transportation code already exists: {code}"` | Duplicate code. |
| `IllegalArgumentException` | `"This registration already exists for the selected provider."` | Duplicate provider and registration number. |
| `WorkflowException` | `"Configuration exceeds capacity!"` | Configured special seats exceed capacity during creation. |

## `importExcel(input)`

### Function signature

```java
public ImportResult importExcel(InputStream input) throws IOException
```

### Parameters

`input` (`InputStream`, required) contains the uploaded Excel workbook.

Reads normalized spreadsheet rows through `ExcelImportUtils`. Each row is converted into `TransportationCreateRequest` and passed to `create`, ensuring imports and normal requests use identical validation. Valid rows are committed and invalid rows are collected as `"Row {row}: {reason}"`. Returns `ImportResult(imported, failed, errors)` and may propagate `IOException` for unreadable files.

Expected columns: `transportationNumber`, `code`, `type`, `providerName`, `totalCapacity`, `agencyId`, optional `branchId`, `premiumSeats`, `accessibleSeats`, and `kidsSeats`.

Import helper failures:

| Helper | Exact message template |
|---|---|
| `required` | `"{field} is required."` |
| `positiveInteger` | `"{field} must be a positive integer."` |
| `optionalInteger` | `"{field} must be a whole number."` |
| `putSeatCount` | `"{chairType} seat count cannot be negative."` or `"{chairType} seat count must be a whole number."` |
| `parseEnum` | `"Invalid {field}: {value}"` |

## `generateSeatLayout(transport, config)`

### Function signature

```java
private List<Seat> generateSeatLayout(Transportation transport, Map<String, Integer> config)
```

### Parameters

`transport` is the owning unit and supplies maximum capacity. `config` maps chair-type names to requested counts and may be `null`.

Creates one physical `Seat` per configured quantity, then fills unused capacity with `STANDARD` seats. `buildSeat` assigns sequential codes (`S1`, `S2`, ...), the requested chair type, `AVAILABLE` status, a zero price modifier, and the parent transportation.

## `update(id, incomingData)`

### Function signature

```java
public Transportation update(Integer id, Transportation incomingData)
```

### Parameters

`id` identifies the managed unit. `incomingData` contains editable scalar values and an optional requested seat layout.

Access requires admin, manager, or owner authority. Copies editable scalar fields while protecting `id`, statuses, seats, calculated inventory, agency relationships, and tours. If `seatConfig` is supplied, `applySeatLayout` reclassifies the existing seats without deleting them.

Seat-layout failures:

- `"Seat layout cannot be changed while seats are reserved, booked, or under maintenance."`
- `"Seat layout cannot be changed while this transportation is assigned to an approved or active tour."`
- `"Unsupported chair type: {type}"`
- `"Seat counts cannot be negative."`
- `"Configured seat counts exceed the transportation capacity of {capacity}."`

## `updateStatus(id, newUnitStatus)`

### Function signature

```java
public Transportation updateStatus(Integer id, TransportationStatus newUnitStatus)
```

### Parameters

`id` identifies the unit and `newUnitStatus` is the requested operational state.

Access requires admin or manager authority. Validates the transition and saves the new operational status.

Failure: `"Cannot force a FULL unit to AVAILABLE. Seats must be freed via ticket cancellations."`

## `filter(filter)`

### Function signature

```java
public PageResponse<Transportation> filter(TransportationFilterRequest filter)
```

### Parameters

`filter` is required and contains type, lifecycle status, unit status, search text, pagination, and sorting.

Builds a JPA specification from transportation type, lifecycle status, unit status, and case-insensitive provider search. Blank search text returns all matching records. Results use the same sort allow-list as `getAll` and are returned as `PageResponse<Transportation>`.
