# User Service

**File:** `src/Api/User.ts`

## Methods

### login(identifier, password) -> AuthResponse
POST `/api/auth/login`

### register(userData) -> AuthResponse
POST `/api/auth/register`

### getAllUsers() -> User[]
GET `/api/users`

### getProfile(userId) -> User
GET `/api/users/{id}`

### updateUser(userId, data) -> User
PUT `/api/users/{id}`

### addEmployee(user, agencyId, branchId) -> User
POST `/api/users/add-employee`

### getAgencyEmployees(agencyId, role?) -> User[]
GET `/api/users/agency/{id}`

### getUsersByRole(type) -> User[]
GET `/api/users/role/{type}`

### deleteUser(userId) -> void
DELETE `/api/users/{id}`

### bulkImport(agencyId, file) -> User[]
POST `/api/users/bulk-import`

### requestPasswordReset(email) -> void
### confirmPasswordReset(email, code, newPassword) -> void
