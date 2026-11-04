# UserRequestController

Base path `/api/user-requests`. Source: `controllers/support/UserRequestController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `POST /api/user-requests` | - | Create. | any signed-in user | body `UserRequestCreateRequest` | `UserRequestResponse` |
| `GET /api/user-requests` | - | Get requests. | any signed-in user | query `filter` | `PageResponse<UserRequestResponse>` |
| `GET /api/user-requests/{id}` | - | Get by id. | any signed-in user | - | `UserRequestResponse` |
| `PATCH /api/user-requests/{id}/assign/{agentId}` | - | Assign. | ADMIN, SUPPORT_AGENT | - | `UserRequestResponse` |
| `PATCH /api/user-requests/{id}/solve` | - | Solve. | any signed-in user | - | `UserRequestResponse` |
| `PATCH /api/user-requests/{id}/reject` | - | REJECT ACTION | ADMIN, SUPPORT_AGENT | - | `UserRequestResponse` |
| `DELETE /api/user-requests/{id}` | - | Delete. | any signed-in user | - | `Void` |
