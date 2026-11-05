# TransportationController

Base path `/api/v1/transportations`. Source: `controllers/tourmanagement/TransportationController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /api/v1/transportations` | - | Create. | OWNER, MANAGER, ADMIN | body `TransportationCreateRequest` | `TransportationResponse` | 400, 401, 403 |
| `POST /api/v1/transportations/imports` | `TransportationImportService.importExcel` | Import excel. | OWNER, MANAGER, ADMIN | - | `ImportResult` | 400, 401, 403 |
| `GET /api/v1/transportations` | - | Get all. | any signed-in user | query `page`, `size`, `sortBy`, `sortDir` | `PageResponse<TransportationResponse>` | 400, 401 |
| `GET /api/v1/transportations/{id}` | - | Get by id. | any signed-in user | - | `TransportationResponse` | 401 |
| `PUT /api/v1/transportations/{id}` | - | Update. | OWNER, MANAGER, ADMIN | body `TransportationUpdateRequest` | `TransportationResponse` | 400, 401, 403 |
| `PATCH /api/v1/transportations/{id}/status` | - | Update status. | OWNER, MANAGER, ADMIN | query `status` | `TransportationResponse` | 400, 401, 403 |
| `GET /api/v1/transportations/search` | - | Search. | any signed-in user | query `filter` | `PageResponse<TransportationResponse>` | 400, 401 |
