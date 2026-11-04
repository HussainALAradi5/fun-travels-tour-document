# AgencyBranchService

Source: `services/agency/AgencyBranchService.java`.

## Functions

### `List<AgencyBranch> getAllBranches()`

**Runs in:** read-only transaction

### `List<AgencyBranch> getBranchesByAgency(Integer agencyId)`

**Runs in:** read-only transaction

### `PageResponse<AgencyBranch> searchBranches(Integer agencyId, String query, Integer page, Integer size)`

**Runs in:** read-only transaction

### `AgencyBranch addBranch(Integer agencyId, AgencyBranchCreateRequest request)`

**Purpose:** Admins add branches anywhere; owners only to their own agency.

**Runs in:** transaction

### `List<User> getEmployeesByBranch(Integer agencyId, Integer branchId)`

**Runs in:** read-only transaction
