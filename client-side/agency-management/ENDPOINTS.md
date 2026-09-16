# Agency Management Client API Usage Endpoints

This table is the feature-owned HTTP contract. Business rules and exception details are documented in this folder's service pages.

| ID | Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|---|
| EP-1 | `POST` | `/api/agencies` | Create an agency and resolve owner/geography references. | Agency payload map | `AgencyService` | `createAgencyFromMap` |
| EP-2 | `GET` | `/api/agencies/{id}` | View one agency. | Numeric agency ID | `AgencyService` | `getAgencyById` |
| EP-3 | `GET` | `/api/agencies/search` | Power the paginated remote agency selector. | `query`, `page`, `size` | `AgencyService` | `searchAgencies` |
| EP-4 | `GET` | `/api/agencies/{id}/employees` | List active agency employees. | Numeric agency ID | `AgencyService` | `getEmployeesByAgencyId` |
| EP-5 | `GET` | `/api/agencies` | Return the legacy complete agency list. | None | `AgencyService` | `getAllAgencies` |
| EP-6 | `POST` | `/api/branches/agency/{agencyId}` | Add a branch to an agency. | Numeric agency ID and branch body | `AgencyBranchService` | `addBranch` |
| EP-7 | `GET` | `/api/branches` | List every branch. | None | `AgencyBranchService` | `getAllBranches` |
| EP-8 | `GET` | `/api/branches/agency/{agencyId}` | List active branches for an agency. | Numeric agency ID | `AgencyBranchService` | `getBranchesByAgency` |
| EP-9 | `GET` | `/api/branches/agency/{agencyId}/search` | Power the paginated remote branch selector. | Agency ID, `query`, `page`, `size` | `AgencyBranchService` | `searchBranches` |
| EP-10 | `GET` | `/api/branches/agency/{agencyId}/branch/{branchId}/employees` | List branch employees after ownership validation. | Agency and branch IDs | `AgencyBranchService` | `getEmployeesByBranch` |

## Endpoint rules

- Authentication and role authorization are enforced by the server.
- Request validation occurs before business-state changes.
- Success and error responses use the shared API envelope.
- Collection endpoints use bounded pagination where supported.

