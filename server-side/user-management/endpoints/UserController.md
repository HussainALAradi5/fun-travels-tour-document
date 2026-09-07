# UserController

**File:** `src/main/java/com/server/server/controllers/UserController.java`
**Base Path:** `/api/users`

## Endpoints

### GET /api/users
Get all active users.
**Access:** ADMIN, MANAGER

### GET /api/users/{id}
Get user by ID.
**Access:** Authenticated

### PUT /api/users/{id}
Update user details.
**Access:** Authenticated (own profile or ADMIN)

### DELETE /api/users/{id}
Delete user.
**Access:** ADMIN

### GET /api/users/role/{type}
Get users by role.
**Access:** ADMIN, MANAGER

### GET /api/users/agency/{id}
Get agency employees.
**Access:** ADMIN, OWNER, MANAGER
**Query Params:** role (optional)

### POST /api/users/add-employee
Add employee to agency.
**Access:** ADMIN, OWNER
**Request Body:**
```json
{
  "user": { },
  "agencyId": 1,
  "branchId": 1
}
```

### POST /api/users/bulk-import
Bulk import users from Excel.
**Access:** ADMIN, OWNER
**Body:** multipart/form-data with file + agencyId
