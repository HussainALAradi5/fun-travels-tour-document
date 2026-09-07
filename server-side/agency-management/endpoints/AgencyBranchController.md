# AgencyBranchController

**File:** `src/main/java/com/server/server/controllers/Agency/AgencyBranchController.java`
**Base Path:** `/api/branches`

## Endpoints

### POST /api/branches
Create a new branch.
**Access:** ADMIN, OWNER

### GET /api/branches/agency/{agencyId}
Get branches by agency.
**Access:** ADMIN, OWNER, MANAGER

### GET /api/branches/{id}/employees
Get branch employees.
**Access:** ADMIN, OWNER, MANAGER
