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

## Detailed behavior and displayed errors

### `getAllBranches()`

- **What should happen:** Return the complete branch collection for administrative use without changing state.
- **Displayed errors:** No deliberate business error; unexpected persistence failures are converted to the generic safe API error.

### `getBranchesByAgency(Integer agencyId)`

- **What should happen:** Return active branches owned by the selected agency.
- **Business rule:** Inactive branches are excluded from customer and employee selectors.
- **Displayed errors:** A null agency ID displays `agencyId must not be null`.

### `searchBranches(Integer agencyId, String query, Integer page, Integer size)`

- **What should happen:** Return a name-sorted, agency-scoped page. Blank search text returns all branches available on that page; entered text performs a case-insensitive name search.
- **Business rule:** A branch from another agency must never be returned in this selector.
- **Displayed errors:** Invalid pagination displays the shared pagination validation message. Unexpected storage errors are hidden behind the generic safe error response.

### `addBranch(Integer agencyId, AgencyBranch branch)`

- **What should happen:** Create one branch under the resolved agency and optionally assign its manager. Both relationship updates succeed together or roll back together.
- **Processing:** Resolve the agency, check name uniqueness inside that agency, set the managed agency, persist the branch, resolve the optional manager, assign the manager's agency and branch, and save the manager.
- **Business rules:** Branch names are unique per agency, but different agencies may use the same name. Client-supplied nested agency/user objects are not trusted as persistence references.
- **Displayed errors:** A duplicate displays `A branch named '{name}' already exists for {agencyName}`. Missing agency or manager displays the standard resource-not-found message. Validation errors display the relevant field message.

### `getEmployeesByBranch(Integer agencyId, Integer branchId)`

- **What should happen:** Return active employees only after confirming that the branch belongs to the requested agency.
- **Business rule:** The ownership check prevents cross-agency employee disclosure.
- **Displayed errors:** A nonexistent branch displays its resource-not-found message. An ownership mismatch displays `This branch does not belong to the specified agency.`
