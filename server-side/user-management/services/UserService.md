# UserService

**File:** `src/main/java/com/server/server/services/UserService.java`

User CRUD and management operations.

## Methods

### getAllUsers() -> List<User>
Fetch all active users.

### getUserById(id) -> User
Fetch user by ID.

### updateUser(id, User) -> User
Update user details.

### deleteUser(id) -> void
Soft-delete user.

### getUsersByRole(UserTypeEnum) -> List<User>
Fetch users by role.

### getAgencyEmployees(agencyId, role?) -> List<User>
Fetch agency staff, optionally filtered by role.

### addEmployee(User, agencyId, branchId) -> User
Create employee with agency assignment.

### bulkImport(agencyId, MultipartFile) -> List<User>
Import users from Excel file.

## Dependencies
- UserRepository
- ExcelImportService
