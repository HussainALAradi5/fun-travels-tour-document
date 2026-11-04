# UserService

Source: `services/user/UserService.java`.

## Business logic

| Function | Rule |
| --- | --- |
| `registerUser` | Unique email, username, and mobile (409); BCrypt-hashed password; wallet opened |
| `createEmployee` | Admin: any role, any agency. Owner: MANAGER/EMPLOYEE in own agency. Manager: EMPLOYEE in own agency/branch. Branch must belong to the agency |
| `updateProfile` | Self or admin only; changes name, mobile, age, photo. Role, agency, email, and password never change here |
| `updatePermissions` | Admin only; role and branch (agency follows the branch) |
| `softDeleteUser` | Admin only; deactivates, cannot deactivate yourself |
| `getAgencyUsers` | Admins, or staff of that agency |
| `bulkImportEmployees` | Rows: username, name, email, password, age, mobile, role, branch. Only MANAGER/EMPLOYEE roles; managers import into their own agency; per-row errors are returned in `ImportResult` |
| `getVisibleUser` | Customers see only themselves; staff can look up users |

## Functions

### `User registerUser(User user, String rawPassword)`

**Purpose:** Saves a new active user with a hashed password and opens their wallet.

**Runs in:** transaction

### `User createEmployee(EmployeeCreateRequest request, Integer agencyId, Integer branchId)`

**Purpose:** Admins create any staff role. Owners create managers and employees in their agency; managers create employees in their agency and branch.

**Runs in:** transaction

### `User updateProfile(Integer id, UserUpdateRequest request)`

**Purpose:** Users edit their own profile; admins edit anyone. Role and agency never change here.

**Runs in:** transaction

### `User updatePermissions(Integer id, UserTypeEnum type, Integer branchId)`

**Runs in:** transaction

### `void softDeleteUser(Integer id)`

**Runs in:** transaction

### `List<User> getAgencyUsers(Integer agencyId, UserTypeEnum type)`

**Purpose:** Agency members are visible to admins and to staff of that agency.

**Runs in:** read-only transaction

### `ImportResult bulkImportEmployees(MultipartFile file, Integer agencyId)`

**Purpose:** Imports staff rows: username, name, email, password, age, mobile, role, branch name. Managers import only into their own agency; only manager and employee roles are accepted.

**Runs in:** transaction

### `User getVisibleUser(Integer id)`

**Purpose:** Self, or any non-customer role (staff need to look up the customers they serve).

**Runs in:** read-only transaction

### `User getUserById(Integer id)`

**Runs in:** read-only transaction

### `List<User> getUsersByType(UserTypeEnum type)`

**Runs in:** read-only transaction

### `User getCurrentUser()`
