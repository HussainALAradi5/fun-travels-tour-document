# TourReservationController

Base path `/api/v1/reservations`. Source: `controllers/tourmanagement/TourReservationController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /api/v1/reservations` | `TourReservationService.create` | Holds places and seats for `BookingRules#HOLD_MINUTES` minutes while payment is pending. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER | body `ReservationCreateRequest` | `ReservationResponse` | 400, 401, 403, 404, 409 (`CUSTOMER_REQUIRED`, `DATE_CONFLICT`) |
| `PATCH /api/v1/reservations/{id}/status` | `TourReservationService.updateStatus` | Update status. | OWNER, MANAGER, ADMIN | query `status` | `ReservationResponse` | 400, 401, 403, 404, 409 (`ALREADY_CANCELLED`) |
| `PATCH /api/v1/reservations/{id}/cancel` | `TourReservationService.cancelReservation` | Customer or staff cancellation. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER | - | `ReservationResponse` | 401, 403, 404, 409 (`ALREADY_CANCELLED`) |
| `GET /api/v1/reservations/search` | `TourReservationService.filter` | Search. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `filter` | `PageResponse<ReservationResponse>` | 400, 401, 403 |
| `GET /api/v1/reservations` | `TourReservationService.getAll` | Get all. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `page`, `size`, `sortDir` | `PageResponse<ReservationResponse>` | 400, 401, 403 |
| `GET /api/v1/reservations/{id}` | `TourReservationService.getById` | Get by id. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `ReservationResponse` | 401, 403, 404 |
