# AgencyBranchService

Source: `services/agency/AgencyBranchService.java`.

## Business logic

- Listing, searching, and the branch staff list are for administrators and the agency's own staff.
- `addBranch`: owners add branches to their own agency, admins to any; names are unique per agency. The optional manager must have the MANAGER role and be unassigned or already in this agency; a manager of another agency is never moved over.

## Functions

### `List<AgencyBranch> getAllBranches()`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `List<AgencyBranch> getBranchesByAgency(Integer agencyId)`

**Purpose:** Active branches, for administrators and the agency's own staff.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Agency not found | `ResourceNotFoundException` | 404 |

### `PageResponse<AgencyBranch> searchBranches(Integer agencyId, String query, Integer page, Integer size)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Agency not found | `ResourceNotFoundException` | 404 |

### `AgencyBranch addBranch(Integer agencyId, AgencyBranchCreateRequest request)`

**Purpose:** Admins add branches anywhere; owners only to their own agency.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Agency not found | `ResourceNotFoundException` | 404 |
| A branch named ' ' already exists for | `DuplicateResourceException` | 409 |
| User not found | `ResourceNotFoundException` | 404 |
| The branch manager must have the MANAGER role. | `IllegalArgumentException` | 400 |
| This manager belongs to another agency. | `IllegalArgumentException` | 400 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `List<User> getEmployeesByBranch(Integer agencyId, Integer branchId)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Branch not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Agency not found | `ResourceNotFoundException` | 404 |
