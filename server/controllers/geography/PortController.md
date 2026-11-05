# PortController

Base path `/api/v1/ports`. Source: `controllers/geography/PortController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/v1/ports` | `PortService.getAllActivePorts` | Get all active ports. | public | - | `List<PortResponse>` | - |
| `POST /api/v1/ports` | `PortService.createPort` | Create port. | ADMIN | body `PortCreateRequest` | `PortResponse` | 400, 401, 403, 404 |
| `PUT /api/v1/ports/{id}/status` | `PortService.updateStatus` | Update status. | ADMIN | query `status` | `PortResponse` | 400, 401, 403, 404 |
