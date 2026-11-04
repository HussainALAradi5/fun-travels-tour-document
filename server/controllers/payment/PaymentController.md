# PaymentController

Base path `/api/payments`. Source: `controllers/payment/PaymentController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `POST /api/payments/execute/{reservationId}` | `TourReservationService.finalizeReservationWithPayment` | Execute payment. | CUSTOMER, ADMIN, MANAGER, OWNER | query `method` | `ReservationResponse` |
| `GET /api/payments` | `PaymentService.filter` | Dynamic filtering with Date support and DESC sorting. | CUSTOMER, ADMIN, MANAGER, OWNER | query `filter` | `PageResponse<PaymentResponse>` |
| `GET /api/payments/{id}` | `PaymentService.getById` | Get by id. | CUSTOMER, ADMIN, MANAGER, OWNER | - | `PaymentResponse` |
