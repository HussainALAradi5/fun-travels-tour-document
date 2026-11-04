# SeatController

Base path `/api/seats`. Source: `controllers/tourmanagement/SeatController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/seats` | `SeatService.getAll` | Get all. | any signed-in user | query `page`, `size`, `sortDir` | `PageResponse<SeatResponse>` |
| `GET /api/seats/{id}` | `SeatService.getById` | Get by id. | any signed-in user | - | `SeatResponse` |
| `PATCH /api/seats/{id}` | `SeatService.updateSeat` | Chair type and price can only change while no active booking or approved/active tour uses the seat. | OWNER, MANAGER, ADMIN | body `SeatUpdateRequest` | `SeatResponse` |
| `GET /api/seats/search` | `SeatService.search` | Lists seats. | any signed-in user | query `filter` | `PageResponse<SeatResponse>` |
| `PATCH /api/seats/{id}/status` | `SeatService.updateStatus` | Update status. | OWNER, MANAGER, ADMIN | query `status` | `SeatResponse` |
