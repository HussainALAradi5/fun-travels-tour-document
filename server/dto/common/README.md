# common DTOs

Source: `dto/common/`. Clients mirror these in `src/dtos/common/`.

## EntityReference

request record. A reference to an existing record by id, sent as `{ "id": 1 `}.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | required; id must be positive |

## GenericFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| `page` | `Integer` | optional |
| `size` | `Integer` | optional |
| `search` | `String` | optional |
| `sortBy` | `String` | optional |
| `sortDir` | `String` | optional |

## ImportResult

response record.

| Field | Type | Rules |
| --- | --- | --- |
| `importedCount` | `int` | - |
| `failedCount` | `int` | - |
| `errors` | `List<String>` | - |

## PageResponse

response record. One page of results with the paging numbers every list endpoint returns.

| Field | Type | Rules |
| --- | --- | --- |
| `content` | `List<T>` | - |
| `page` | `int` | - |
| `size` | `int` | - |
| `totalElements` | `long` | - |
| `totalPages` | `int` | - |
