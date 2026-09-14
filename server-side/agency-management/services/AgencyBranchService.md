# Agency Branch Service

**Source:** `src/main/java/com/server/server/services/agency/AgencyBranchService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions / authorization |
|---|---|---|---|---|---|
| `public List<AgencyBranch> getAllBranches()` | None | Calls `findAll`. | Supports complete branch administration. | All branches; read-only. | None directly. |
| `public List<AgencyBranch> getBranchesByAgency(Integer agencyId)` | Required agency ID | Queries active branches by agency. | Selectors exclude inactive branches. | Active branches; read-only. | Null: `"agencyId must not be null"`. |
| `public PageResponse<AgencyBranch> searchBranches(Integer agencyId, String query, Integer page, Integer size)` | Agency ID, optional query/page/size | Trims query, orders by name, returns all agency branches for blank input or name matches otherwise. | Server-backed selectors are agency-scoped and show the first page without search text. | One page; read-only. | Pagination errors may propagate. |
| `public AgencyBranch addBranch(Integer agencyId, AgencyBranch branch)` | Parent ID and branch aggregate | Resolves agency, checks name uniqueness, sets owner, saves, then links an optional manager. | Branch names are unique per agency and managers inherit agency/branch assignment. | Created branch; writes branch and optional user. | Missing agency/user resource errors; `"A branch named '{name}' already exists for {agencyName}"`. |
| `public List<User> getEmployeesByBranch(Integer agencyId, Integer branchId)` | Required agency and branch IDs | Resolves branch, verifies ownership, then queries active employees. | Prevents cross-agency data access. | Active employees; read-only. | Missing branch resource error; `SecurityException`: `"This branch does not belong to the specified agency."` |

Read functions are read-only transactions; `addBranch` is transactional.
