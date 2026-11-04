# UserService

Source: `services/user/UserService.java`.

## Business logic

| Function | Rule |
| --- | --- |
| `registerUser` | Unique email, username, and mobile (409); BCrypt-hashed password; wallet opened |
| `createEmployee` | Admin: any role, any agency. Owner: MANAGER/EMPLOYEE in own agency. Manager: EMPLOYEE in own agency and always in the manager's own branch. Branch must belong to the agency |
| `updateProfile` | Self or admin only; changes name, mobile (stored without spaces, country code required), age, photo. A new photo gets a new file name and the old file is deleted; removing the photo deletes the file. Role, agency, email, and password never change here |
| `updatePermissions` | Admin only, never on yourself. Agency staff must end up in an agency (from the branch, or `agencyId` for owners); a branch must belong to that agency; other roles leave any agency |
| `softDeleteUser` | Admin only; deactivates, cannot deactivate yourself |
| `getUsersByType` | Admins see every active user. Agency staff see their agency's members, and customers when they ask for that role (walk-in ticket sales) |
| `getAgencyUsers` | Admins, or staff of that agency |
| `bulkImportEmployees` | Rows: username, name, email, password, age, mobile, role, branch. Owners/admins import MANAGER and EMPLOYEE; managers import EMPLOYEE only, into their own branch; per-row errors are returned in `ImportResult` |
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

### `User updatePermissions(Integer id, UserTypeEnum type, Integer agencyId, Integer branchId)`

**Purpose:** Admin-only role and placement change. Agency staff must end up in an agency (taken from the branch, or from `agencyId` for owners who have no branch); other roles leave any agency.

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

**Purpose:** Admins see every active user. Agency staff see their own agency's members, and customers when they ask for that role, because staff sell walk-in tickets to customers.

**Runs in:** read-only transaction

### `User getCurrentUser()`
