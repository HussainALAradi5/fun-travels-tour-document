# PaymentController

Base path `/api/payments`. Source: `controllers/payment/PaymentController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /api/payments/execute/{reservationId}` | `TourReservationService.finalizeReservationWithPayment` | Execute payment. | CUSTOMER, ADMIN, MANAGER, OWNER | query `method` | `ReservationResponse` | 400, 401, 403, 409 |
| `GET /api/payments` | `PaymentService.filter` | Dynamic filtering with Date support and DESC sorting. | CUSTOMER, ADMIN, MANAGER, OWNER | query `filter` | `PageResponse<PaymentResponse>` | 400, 401, 403 |
| `GET /api/payments/{id}` | `PaymentService.getById` | Get by id. | CUSTOMER, ADMIN, MANAGER, OWNER | - | `PaymentResponse` | 401, 403, 404 |
