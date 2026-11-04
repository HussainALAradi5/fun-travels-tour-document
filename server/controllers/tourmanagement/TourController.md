# TourController

Base path `/api/tours`. Source: `controllers/tourmanagement/TourController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/tours/catalog` | `TourService.getCatalogTours` | Get catalog. | public | query `startCountryId`, `endCountryId`, `startDate`, `endDate`, `page`, `size` | `PageResponse<TourResponse>` |
| `GET /api/tours/search` | `TourService.filter` | Search. | public | query `filter` | `PageResponse<TourResponse>` |
| `GET /api/tours` | `TourService.getAll` | Get all. | public | query `page`, `size`, `sortBy`, `sortDir` | `PageResponse<TourResponse>` |
| `GET /api/tours/{id}` | `TourService.getById` | Get by id. | public | - | `TourResponse` |
| `POST /api/tours` | `TourService.create` | Create. | OWNER, MANAGER, ADMIN | body `TourCreateRequest` | `TourResponse` |
| `PUT /api/tours/{id}` | `TourService.updateTour` | Update. | OWNER, MANAGER, ADMIN | body `TourUpdateRequest` | `TourResponse` |
| `PUT /api/tours/{id}/status` | `TourService.updateStatus` | Update status. | OWNER, MANAGER, ADMIN | query `status` | `TourResponse` |
