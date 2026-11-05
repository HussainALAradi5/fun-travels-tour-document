# TourController

Base path `/api/v1/tours`. Source: `controllers/tourmanagement/TourController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/v1/tours/catalog` | `TourCatalogService.getCatalogTours` | Get catalog. | public | query `startCountryId`, `endCountryId`, `startDate`, `endDate`, `page`, `size` | `PageResponse<TourResponse>` | 400 |
| `GET /api/v1/tours/search` | `TourCatalogService.filter` | Search. | public | query `filter` | `PageResponse<TourResponse>` | 400 |
| `GET /api/v1/tours` | `TourCatalogService.getAll` | Admins and agency staff list every tour (staff within their agency); everyone else only bookable ones. | public | query `page`, `size`, `sortBy`, `sortDir` | `PageResponse<TourResponse>` | 400 |
| `GET /api/v1/tours/{id}` | `TourCatalogService.getVisible` | One tour by id for the public endpoint. | public | - | `TourResponse` | 404 |
| `POST /api/v1/tours` | `TourService.create` | Create. | OWNER, MANAGER, ADMIN | body `TourCreateRequest` | `TourResponse` | 400, 401, 403, 404, 409 (`DISCOUNT_ABOVE_PRICE`, `MEAL_INACTIVE`, `MEAL_OTHER_AGENCY`) |
| `PUT /api/v1/tours/{id}` | `TourService.updateTour` | Update. | OWNER, MANAGER, ADMIN | body `TourUpdateRequest` | `TourResponse` | 400, 401, 403, 404, 409 (`CAPACITY_BELOW_BOOKINGS`, `DISCOUNT_ABOVE_PRICE`, `MEAL_INACTIVE`, `MEAL_OTHER_AGENCY`, `TRANSPORTATION_LOCKED`) |
| `PUT /api/v1/tours/{id}/status` | `TourStatusService.updateStatus` | Update status. | OWNER, MANAGER, ADMIN | query `status` | `TourResponse` | 400, 401, 403, 409 |
