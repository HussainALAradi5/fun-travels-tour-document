# UserController

**File:** `src/main/java/com/server/server/controllers/UserController.java`
**Base Path:** `/api/users`

## Endpoints

### GET /api/users

**Description:** Get all active users

**Service Method:** `UserService.getUsersByType(null)`

**Response:** `200 OK` - List of User entities

**Access:** Authenticated

---

### GET /api/users/{id}

**Description:** Get user by ID

**Service Method:** `UserService.getUserById(id)`

**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | User ID |

**Response:** `200 OK` - User entity

**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | "User not found or inactive." |

**Access:** Authenticated

---

### GET /api/users/agency/{agencyId}

**Description:** Get agency employees, optionally filtered by role

**Service Method:** `UserService.getAgencyUsers(agencyId, role)`

**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| agencyId | Integer | Agency ID |

**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| role | UserTypeEnum | No | Filter by role |

**Response:** `200 OK` - List of User entities

**Access:** Authenticated

---

### PUT /api/users/{id}

**Description:** Update user details

**Service Method:** `UserService.updateUser(id, user)`

**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | User ID |

**Request Body:** User entity with updated fields

**Response (200 OK):**
```json
{
  "success": true,
  "message": "User updated successfully!",
  "data": { }
}
```

**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | "User not found or inactive." |

**Access:** Authenticated (own profile or ADMIN)

---

### POST /api/users/bulk-import

**Description:** Bulk import users from Excel file

**Service Method:** `UserService.bulkImportEmployees(file, agencyId)`

**Request:** multipart/form-data

**Body Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| file | MultipartFile | Yes | Excel file (.xlsx) |
| agencyId | Integer | Yes | Target agency ID |

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Bulk import successful!",
  "data": []
}
```

**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Agency not found, invalid file format |

**Access:** MANAGER, ADMIN

---

### PUT /api/users/permissions/{id}

**Description:** Update user role and branch assignment

**Service Method:** `UserService.updatePermissions(id, type, branchId)`

**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | User ID |

**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| type | UserTypeEnum | Yes | New role |
| branchId | Integer | No | Branch ID (null to unassign) |

**Access:** ADMIN

---

### DELETE /api/users/{id}

**Description:** Soft-delete (deactivate) a user

**Service Method:** `UserService.softDeleteUser(id)`

**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | User ID |

**Response (200 OK):**
```json
{
  "success": true,
  "message": "User deactivated successfully"
}
```

**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | "User not found or inactive." |

**Access:** ADMIN

---

### GET /api/users/role/{type}

**Description:** Get users by role type

**Service Method:** `UserService.getUsersByType(type)`

**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| type | UserTypeEnum | Role type |

**Response:** `200 OK` - List of User entities

**Access:** Authenticated

---

### POST /api/users/request-password-reset

**Description:** Request password reset code via email

**Service Method:** `UserService.requestPasswordReset(identifier, baseNumber)`

**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| identifier | String | Yes | Email address |
| baseNumber | String | No | Mobile number fallback |

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Reset code sent successfully!"
}
```

**Access:** Public

---

### POST /api/users/confirm-password-reset

**Description:** Confirm password reset with token

**Service Method:** `UserService.confirmPasswordReset(identifier, baseNumber, token, newPassword)`

**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| identifier | String | Yes | Email address |
| baseNumber | String | No | Mobile number |
| token | String | Yes | Reset token from email |
| newPassword | String | Yes | New password |

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Password reset successfully!"
}
```

**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Invalid/expired reset link, user not found |

**Access:** Public
