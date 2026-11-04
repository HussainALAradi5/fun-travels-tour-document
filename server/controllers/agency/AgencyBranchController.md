# AgencyBranchController

Base path `/api/branches`. Source: `controllers/agency/AgencyBranchController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `POST /api/branches/agency/{agencyId}` | `AgencyBranchService.addBranch` | Admins add branches anywhere; owners only to their own agency. | ADMIN, OWNER | body `AgencyBranchCreateRequest` | `AgencyBranchResponse` |
| `GET /api/branches` | `AgencyBranchService.getAllBranches` | Get all branches. | ADMIN | - | `List<AgencyBranchResponse>` |
| `GET /api/branches/agency/{agencyId}` | `AgencyBranchService.getBranchesByAgency` | Active branches, for administrators and the agency's own staff. | any signed-in user | - | `List<AgencyBranchResponse>` |
| `GET /api/branches/agency/{agencyId}/search` | `AgencyBranchService.searchBranches` | Search by agency. | any signed-in user | query `query`, `page`, `size` | `PageResponse<AgencyBranchResponse>` |
| `GET /api/branches/agency/{agencyId}/branch/{branchId}/employees` | `AgencyBranchService.getEmployeesByBranch` | Get employees by agency and branch. | any signed-in user | - | `List<UserResponse>` |
