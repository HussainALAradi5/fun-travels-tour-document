# TransportationController

Base path `/api/transportations`. Source: `controllers/tourmanagement/TransportationController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `POST /api/transportations` | - | Create. | OWNER, MANAGER, ADMIN | body `TransportationCreateRequest` | `TransportationResponse` |
| `POST /api/transportations/imports` | - | Import excel. | OWNER, MANAGER, ADMIN | - | `ImportResult` |
| `GET /api/transportations` | - | Get all. | any signed-in user | query `page`, `size`, `sortBy`, `sortDir` | `PageResponse<TransportationResponse>` |
| `GET /api/transportations/{id}` | - | Get by id. | any signed-in user | - | `TransportationResponse` |
| `PUT /api/transportations/{id}` | - | Update. | OWNER, MANAGER, ADMIN | body `TransportationUpdateRequest` | `TransportationResponse` |
| `PATCH /api/transportations/{id}/status` | - | Update status. | OWNER, MANAGER, ADMIN | query `status` | `TransportationResponse` |
| `GET /api/transportations/search` | - | Search. | any signed-in user | query `filter` | `PageResponse<TransportationResponse>` |
