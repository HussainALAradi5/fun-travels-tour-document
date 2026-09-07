# UserService

**File:** `src/main/java/com/server/server/services/UserService.java`

## Methods

### createUser(User) -> User

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| user | User | User entity with registration data |

**Returns:** Saved User entity with generated ID

**Business Logic:**
1. Validates email uniqueness (throws if taken)
2. Validates username uniqueness (throws if taken)
3. Encodes password with BCrypt
4. Sets active = true
5. Saves user to database
6. Auto-provisions digital wallet via AccountService
7. Links account to user object

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Email taken" - email already exists |
| RuntimeException | "Username taken" - username already exists |

---

### login(identifier, password) -> User

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| identifier | String | Email, username, or mobile number |
| password | String | Plain text password |

**Returns:** User entity if authenticated

**Business Logic:**
1. Searches user by email (case-insensitive)
2. Falls back to username (case-insensitive)
3. Falls back to mobile number
4. Filters by active = true
5. Validates password against BCrypt hash

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Invalid credentials or inactive account." |
| RuntimeException | "Wrong password." |

---

### updateUser(id, User) -> User

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | User ID to update |
| user | User | User entity with updated fields |

**Returns:** Updated User entity

**Business Logic:**
1. Fetches existing user by ID
2. Copies properties (excluding id, password, userName, profileImageUrl, agency, agencyBranch)
3. If base64Image provided, saves image and updates profileImageUrl
4. Saves and flushes to database

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "User not found or inactive." |

---

### softDeleteUser(id) -> void

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | User ID to deactivate |

**Returns:** void

**Business Logic:**
1. Fetches user by ID
2. Sets active = false
3. Removes agency/branch associations
4. Saves to database

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "User not found or inactive." |

---

### requestPasswordReset(email, baseNumber) -> String

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| email | String | User's email address |
| baseNumber | String | Optional mobile number fallback |

**Returns:** Success message string

**Business Logic:**
1. Finds user by email (case-insensitive)
2. Filters by active = true
3. Generates UUID token
4. Sets reset token and 15-minute expiry on user
5. Sends HTML reset email with link

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Account with this email was not found." |
| RuntimeException | "Error sending email: ..." |

---

### confirmPasswordReset(identifier, baseNumber, token, newPassword) -> User

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| identifier | String | Email address |
| baseNumber | String | Optional mobile number |
| token | String | Reset token from email |
| newPassword | String | New password to set |

**Returns:** Updated User entity

**Business Logic:**
1. Finds user by email or mobile
2. Validates reset token matches
3. Validates token hasn't expired (15 min)
4. Encodes new password with BCrypt
5. Clears reset token and expiry
6. Saves user

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "User not found or inactive." |
| RuntimeException | "Invalid or expired reset link." |
| RuntimeException | "Reset link expired." |

---

### getAgencyUsers(agencyId, type) -> List<User>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| agencyId | Integer | Agency ID |
| type | UserTypeEnum | Optional role filter |

**Returns:** List of active users in agency

---

### getUsersByType(type) -> List<User>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| type | UserTypeEnum | Optional role filter (null = all) |

**Returns:** List of active users filtered by role

---

### getCurrentUser() -> User

**Parameters:** None

**Returns:** Currently authenticated User or null

**Business Logic:**
1. Gets Authentication from SecurityContext
2. If anonymous, returns null
3. Finds user by email from authentication principal
4. Filters by active = true

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Authenticated user not found or inactive." |

---

### bulkImportEmployees(file, agencyId) -> List<User>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| file | MultipartFile | Excel file (.xlsx) |
| agencyId | Integer | Target agency ID |

**Returns:** List of created User entities

**Business Logic:**
1. Validates agency exists
2. Parses Excel file via ExcelImportService
3. Maps columns: username, name, email, password, age, mobile, role, branch
4. Encodes passwords with BCrypt
5. Links to agency and branch
6. Filters out duplicate emails
7. Saves all valid users

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Agency required" - agency not found |
