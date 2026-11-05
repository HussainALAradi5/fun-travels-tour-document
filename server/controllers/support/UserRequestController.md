# UserRequestController

Base path `/api/v1/user-requests`. Source: `controllers/support/UserRequestController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /api/v1/user-requests` | - | Create. | any signed-in user | body `UserRequestCreateRequest` | `UserRequestResponse` | 400, 401 |
| `GET /api/v1/user-requests` | - | Get requests. | any signed-in user | query `filter` | `PageResponse<UserRequestResponse>` | 400, 401 |
| `GET /api/v1/user-requests/{id}` | - | Get by id. | any signed-in user | - | `UserRequestResponse` | 401 |
| `PATCH /api/v1/user-requests/{id}/assign/{agentId}` | - | Assign. | ADMIN, SUPPORT_AGENT | - | `UserRequestResponse` | 401, 403 |
| `PATCH /api/v1/user-requests/{id}/solve` | - | Solve. | any signed-in user | - | `UserRequestResponse` | 401 |
| `PATCH /api/v1/user-requests/{id}/reject` | - | REJECT ACTION | ADMIN, SUPPORT_AGENT | - | `UserRequestResponse` | 401, 403 |
| `DELETE /api/v1/user-requests/{id}` | - | Delete. | any signed-in user | - | `Void` | 401 |
