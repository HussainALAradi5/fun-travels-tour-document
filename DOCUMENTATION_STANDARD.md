# Documentation Standard

This repository documents behavior that a maintainer needs to safely change the system. Every service page follows the same method-level structure.

## Required function structure

Every documented function uses the following sections in this exact order:

1. **Function name** — a heading containing the method name.
2. **Function signature** — the exact Java or TypeScript declaration in a code block.
3. **Purpose** — the responsibility of the function in one concise paragraph.
4. **Parameters** — a table containing name, type, required/nullability, and meaning.
5. **Return value** — the type, meaning, and important empty/null behavior.
6. **Function logic** — implementation steps in execution order.
7. **Business logic** — domain rules and the reason those rules exist.
8. **Side effects** — database writes, locks, notifications, external calls, or state changes.
9. **Exceptions** — exception type, stable code when present, exact message, and condition.
10. **Authorization and transaction behavior** — required roles and transactional guarantees.

Use `None directly` in the exceptions section when a function has no explicit failure. Also list important exceptions propagated from called business services. Do not write only `throws RuntimeException`; document the useful message and its triggering condition.

### Function template

````markdown
## `functionName`

### Function signature

```java
ReturnType functionName(ParameterType parameter)
```

### Purpose

...

### Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|

### Return value

...

### Function logic

1. ...

### Business logic

- ...

### Side effects

- ...

### Exceptions

| Exception/code | Exact message | Condition |
|---|---|---|

### Authorization and transaction

...
````

Private helpers are documented when they implement validation, calculations, mapping, locking, scheduled work, or user-visible failures. Trivial predicate builders and framework-generated accessors may be grouped to keep pages readable.

## Message notation

- Text in quotation marks is the exact current message.
- Values in braces are runtime substitutions, for example `"Seat {seatCode} is no longer available."`.
- A code such as `INSUFFICIENT_CAPACITY` is part of the stable API error contract.
- Messages without a stable code currently use the global fallback code selected by `GlobalExceptionHandler`.

## Shared response contract

Controllers return `ApiResponse<T>`. Failures expose `success`, `code`, `message`, `data`, `fieldErrors`, `timestamp`, and `path`. Paginated data uses `PageResponse<T>` with `content`, `page`, `size`, `totalElements`, and `totalPages`.

## Maintenance rule

When service behavior changes, update its service page in the same change. Endpoint pages describe transport-level contracts; service pages remain the source of truth for business logic and failure conditions.
