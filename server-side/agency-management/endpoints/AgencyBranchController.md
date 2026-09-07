# AgencyBranchController

**File:** `src/main/java/com/server/server/controllers/agency/AgencyBranchController.java`
**Base Path:** `/api/branches`

## Endpoints

### POST /api/branches/agency/{agencyId}

**Description:** Add a branch to an agency
**Service Method:** `AgencyBranchService.addBranch(agencyId, branch)`
**Path Params:** agencyId (Integer) - Agency ID
**Request Body:**
```json
{
  "branchName": "string",
  "branchAddress": "string",
  "contactNumber": "string",
  "branchManager": { "id": 1 }
}
```
**Response (200 OK):** Created AgencyBranch entity
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Agency not found, branch name already exists |
**Access:** ADMIN, OWNER

---

### GET /api/branches

**Description:** Get all branches
**Service Method:** `AgencyBranchService.getAllBranches()`
**Response (200 OK):** List of AgencyBranch entities
**Access:** Public

---

### GET /api/branches/agency/{agencyId}

**Description:** Get branches by agency
**Service Method:** `AgencyBranchService.getBranchesByAgency(agencyId)`
**Path Params:** agencyId (Integer) - Agency ID
**Response (200 OK):** List of AgencyBranch entities
**Access:** Public

---

### GET /api/branches/agency/{agencyId}/branch/{branchId}/employees

**Description:** Get employees for a specific branch
**Service Method:** `AgencyBranchService.getEmployeesByBranch(agencyId, branchId)`
**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| agencyId | Integer | Agency ID (security check) |
| branchId | Integer | Branch ID |
**Response (200 OK):** List of User entities
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Branch not found, security mismatch |
**Access:** ADMIN, OWNER, MANAGER
