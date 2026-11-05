# AgencyController

Base path `/api/v1/agencies`. Source: `controllers/agency/AgencyController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /api/v1/agencies` | `AgencyService.createAgency` | Admin-only. | ADMIN | body `AgencyCreateRequest` | `AgencyResponse` | 400, 401, 403, 404, 409 |
| `GET /api/v1/agencies/{id}` | `AgencyService.getVisibleAgency` | Agency details (owner contacts included) for administrators and the agency's own staff. | any signed-in user | - | `AgencyResponse` | 401, 403, 404 |
| `GET /api/v1/agencies/search` | `AgencyService.searchAgencies` | Admins search every agency; agency staff find only their own; other roles are refused. | any signed-in user | query `query`, `page`, `size` | `PageResponse<AgencyResponse>` | 400, 401, 403 |
| `GET /api/v1/agencies/{id}/employees` | `AgencyService.getEmployeesByAgencyId` | Get employees by agency. | any signed-in user | - | `List<UserResponse>` | 401, 403, 404 |
| `GET /api/v1/agencies` | `AgencyService.getAllAgencies` | Admins see every agency; agency staff only their own. | ADMIN, OWNER, MANAGER, EMPLOYEE | - | `List<AgencyResponse>` | 401, 403, 404 |
