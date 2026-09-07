# UserRequestController

**File:** `src/main/java/com/server/server/controllers/UserRequestController.java`
**Base Path:** `/api/requests`

## Endpoints

### POST /api/requests
Create support request.
**Access:** Authenticated

### GET /api/requests
Get requests with pagination.
**Access:** Authenticated (filtered by role)

### GET /api/requests/{id}
**Access:** Authenticated (own or admin/support)

### PATCH /api/requests/{id}/assign
**Access:** ADMIN, SUPPORT_AGENT

### PATCH /api/requests/{id}/solve
**Access:** ADMIN, SUPPORT_AGENT

### PATCH /api/requests/{id}/reject
**Access:** ADMIN, SUPPORT_AGENT

### DELETE /api/requests/{id}
**Access:** ADMIN
