# TicketController

Base path `/api/tickets`. Source: `controllers/tourmanagement/TicketController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/tickets/search` | `TicketService.filter` | Search. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `filter` | `PageResponse<TicketResponse>` | 400, 401, 403 |
| `GET /api/tickets` | `TicketService.getAll` | Get all. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `page`, `size`, `sortDir` | `PageResponse<TicketResponse>` | 400, 401, 403 |
| `GET /api/tickets/{id}/refund-quote` | `TicketService.refundQuote` | What cancelling this ticket now would refund, shown before the customer confirms. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `RefundQuoteResponse` | 401, 403, 404 |
| `GET /api/tickets/{id}` | `TicketService.getById` | Get by id. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `TicketResponse` | 401, 403, 404 |
| `POST /api/tickets` | `TicketService.create` | Staff-issued walk-in ticket for an existing customer. | ADMIN, MANAGER, EMPLOYEE, OWNER | body `TicketCreateRequest` | `TicketResponse` | 400, 401, 403, 404 |
| `PUT /api/tickets/{id}/status` | `TicketService.updateStatus` | Staff progress a paid ticket: APPROVED, CONFIRMED, or COMPLETED. | OWNER, MANAGER, ADMIN | query `status` | `TicketResponse` | 400, 401, 403, 404, 409 |
| `PUT /api/tickets/{id}/cancel` | `TicketService.cancelTicket` | Cancels one ticket. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER | - | `TicketResponse` | 401, 403, 404, 409 |
| `PUT /api/tickets/{id}/approve` | `TicketService.updateStatus` | Staff progress a paid ticket: APPROVED, CONFIRMED, or COMPLETED. | OWNER, MANAGER, ADMIN | - | `TicketResponse` | 401, 403, 404, 409 |
| `PUT /api/tickets/{id}/confirm` | `TicketService.updateStatus` | Staff progress a paid ticket: APPROVED, CONFIRMED, or COMPLETED. | OWNER, MANAGER, ADMIN | - | `TicketResponse` | 401, 403, 404, 409 |
