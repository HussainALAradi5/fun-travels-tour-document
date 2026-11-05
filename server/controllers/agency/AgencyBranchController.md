# AgencyBranchController

Base path `/api/v1/branches`. Source: `controllers/agency/AgencyBranchController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /api/v1/branches/agency/{agencyId}` | `AgencyBranchService.addBranch` | Admins add branches anywhere; owners only to their own agency. | ADMIN, OWNER | body `AgencyBranchCreateRequest` | `AgencyBranchResponse` | 400, 401, 403, 404, 409 |
| `GET /api/v1/branches` | `AgencyBranchService.getAllBranches` | Get all branches. | ADMIN | - | `List<AgencyBranchResponse>` | 401, 403 |
| `GET /api/v1/branches/agency/{agencyId}` | `AgencyBranchService.getBranchesByAgency` | Active branches, for administrators and the agency's own staff. | any signed-in user | - | `List<AgencyBranchResponse>` | 401, 403, 404 |
| `GET /api/v1/branches/agency/{agencyId}/search` | `AgencyBranchService.searchBranches` | Search by agency. | any signed-in user | query `query`, `page`, `size` | `PageResponse<AgencyBranchResponse>` | 400, 401, 403, 404 |
| `GET /api/v1/branches/agency/{agencyId}/branch/{branchId}/employees` | `AgencyBranchService.getEmployeesByBranch` | Get employees by agency and branch. | any signed-in user | - | `List<UserResponse>` | 401, 403, 404 |
