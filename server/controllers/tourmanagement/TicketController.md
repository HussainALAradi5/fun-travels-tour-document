# TicketController

Base path `/api/tickets`. Source: `controllers/tourmanagement/TicketController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/tickets/search` | `TicketService.filter` | Search. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `filter` | `PageResponse<TicketResponse>` |
| `GET /api/tickets` | `TicketService.getAll` | Get all. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `page`, `size`, `sortDir` | `PageResponse<TicketResponse>` |
| `GET /api/tickets/{id}` | `TicketService.getById` | Get by id. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `TicketResponse` |
| `POST /api/tickets` | `TicketService.create` | Staff-issued walk-in ticket for an existing customer. | ADMIN, MANAGER, EMPLOYEE, OWNER | body `TicketCreateRequest` | `TicketResponse` |
| `PUT /api/tickets/{id}/status` | `TicketService.updateStatus` | Staff progress a paid ticket: APPROVED, CONFIRMED, or COMPLETED. | OWNER, MANAGER, ADMIN | query `status` | `TicketResponse` |
| `PUT /api/tickets/{id}/cancel` | `TicketService.cancelTicket` | Cancels one ticket. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER | - | `TicketResponse` |
| `PUT /api/tickets/{id}/approve` | `TicketService.updateStatus` | Staff progress a paid ticket: APPROVED, CONFIRMED, or COMPLETED. | OWNER, MANAGER, ADMIN | - | `TicketResponse` |
| `PUT /api/tickets/{id}/confirm` | `TicketService.updateStatus` | Staff progress a paid ticket: APPROVED, CONFIRMED, or COMPLETED. | OWNER, MANAGER, ADMIN | - | `TicketResponse` |
