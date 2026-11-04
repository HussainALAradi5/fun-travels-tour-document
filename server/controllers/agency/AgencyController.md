# AgencyController

Base path `/api/agencies`. Source: `controllers/agency/AgencyController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `POST /api/agencies` | `AgencyService.createAgency` | Admin-only. | ADMIN | body `AgencyCreateRequest` | `AgencyResponse` |
| `GET /api/agencies/{id}` | `AgencyService.getAgencyById` | Get by id. | any signed-in user | - | `AgencyResponse` |
| `GET /api/agencies/search` | `AgencyService.searchAgencies` | Search. | any signed-in user | query `query`, `page`, `size` | `PageResponse<AgencyResponse>` |
| `GET /api/agencies/{id}/employees` | `AgencyService.getEmployeesByAgencyId` | Get employees by agency. | any signed-in user | - | `List<UserResponse>` |
| `GET /api/agencies` | `AgencyService.getAllAgencies` | Get all. | ADMIN, OWNER, MANAGER, EMPLOYEE | - | `List<AgencyResponse>` |
