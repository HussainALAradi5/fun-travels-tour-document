# TourReservationController

Base path `/api/reservations`. Source: `controllers/tourmanagement/TourReservationController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `POST /api/reservations` | `TourReservationService.create` | Holds places and seats for `BookingRules#HOLD_MINUTES` minutes while payment is pending. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER | body `ReservationCreateRequest` | `ReservationResponse` |
| `PATCH /api/reservations/{id}/status` | `TourReservationService.updateStatus` | Update status. | OWNER, MANAGER, ADMIN | query `status` | `ReservationResponse` |
| `PATCH /api/reservations/{id}/cancel` | `TourReservationService.cancelReservation` | Customer or staff cancellation. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER | - | `ReservationResponse` |
| `GET /api/reservations/search` | `TourReservationService.filter` | Search. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `filter` | `PageResponse<ReservationResponse>` |
| `GET /api/reservations` | `TourReservationService.getAll` | Get all. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `page`, `size`, `sortDir` | `PageResponse<ReservationResponse>` |
| `GET /api/reservations/{id}` | `TourReservationService.getById` | Get by id. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `ReservationResponse` |
