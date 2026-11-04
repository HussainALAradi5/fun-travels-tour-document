# AgencyBranchService

Source: `services/agency/AgencyBranchService.java`.

## Business logic

- Listing, searching, and the branch staff list are for administrators and the agency's own staff.
- `addBranch`: owners add branches to their own agency, admins to any; names are unique per agency. The optional manager must have the MANAGER role and be unassigned or already in this agency; a manager of another agency is never moved over.

## Functions

### `List<AgencyBranch> getAllBranches()`

**Runs in:** read-only transaction

### `List<AgencyBranch> getBranchesByAgency(Integer agencyId)`

**Purpose:** Active branches, for administrators and the agency's own staff.

**Runs in:** read-only transaction

### `PageResponse<AgencyBranch> searchBranches(Integer agencyId, String query, Integer page, Integer size)`

**Runs in:** read-only transaction

### `AgencyBranch addBranch(Integer agencyId, AgencyBranchCreateRequest request)`

**Purpose:** Admins add branches anywhere; owners only to their own agency.

**Runs in:** transaction

### `List<User> getEmployeesByBranch(Integer agencyId, Integer branchId)`

**Runs in:** read-only transaction
