# PortController

Base path `/api/ports`. Source: `controllers/geography/PortController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/ports` | `PortService.getAllActivePorts` | Get all active ports. | public | - | `List<PortResponse>` |
| `POST /api/ports` | `PortService.createPort` | Create port. | ADMIN | body `PortCreateRequest` | `PortResponse` |
| `PUT /api/ports/{id}/status` | `PortService.updateStatus` | Update status. | ADMIN | query `status` | `PortResponse` |
