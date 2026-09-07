# AgencyController

**File:** `src/main/java/com/server/server/controllers/Agency/AgencyController.java`
**Base Path:** `/api/agencies`

## Endpoints

### GET /api/agencies
Get all agencies.
**Access:** Public

### GET /api/agencies/{id}
Get agency by ID.
**Access:** Public

### POST /api/agencies
Create a new agency.
**Access:** ADMIN, OWNER

### PUT /api/agencies/{id}
Update agency details.
**Access:** ADMIN, OWNER

### GET /api/agencies/{id}/employees
Get agency employees.
**Access:** ADMIN, OWNER, MANAGER
