# Seat API

**Controller:** `SeatController`

**Base path:** `/api/seats`

All successful responses use `ApiResponse<T>`. Collection endpoints return `PageResponse<SeatResponse>` inside the `data` field.

| Method | Path | Purpose | Access |
|---|---|---|---|
| `GET` | `/api/seats` | List seats with `page`, `size`, and `sortDir`. | Authenticated |
| `GET` | `/api/seats/{id}` | Get one seat. | Authenticated |
| `GET` | `/api/seats/search` | Search and filter seats with `SeatFilterRequest`. | Authenticated |
| `PATCH` | `/api/seats/{id}` | Update configurable seat details. | Owner, manager, admin |
| `PATCH` | `/api/seats/{id}/status?status=AVAILABLE` | Update seat status. | Owner, manager, admin |

## Search parameters

`transportId`, `status`, `chairType`, `keyword` (or `search`), `page`, `size`, `sortBy`, and `sortDir` are supported. Omitting filters returns all seats in the requested page.

## Notes

- Static `/search` routing is distinct from numeric `/{id}` lookup.
- Seat configuration failures are returned as user-readable workflow errors.
- `SeatResponse` prevents persistence entities and lazy proxies from leaking into the public API.
