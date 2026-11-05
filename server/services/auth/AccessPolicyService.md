# AccessPolicyService

Source: `services/auth/AccessPolicyService.java`.

Central ownership and tenancy rules. Controllers check roles; this service checks whose data a signed-in user may read or change.

## Business logic

Controllers check roles; this service checks whose data a signed-in user may touch.

| Rule | Behavior |
| --- | --- |
| `requireSelfOrAdmin(userId)` | Wallet, notifications, profile edits |
| `requireRecordAccess(user, ownerId, agency)` | Customers: only their own record. Agency staff (OWNER, MANAGER, EMPLOYEE): only their agency. Admin and support: unrestricted |
| `agencyScope(user)` | Agency id applied to list queries for agency staff; staff without an agency are rejected |
| `requireAgencyMember(user, agency)` | Stricter: only administrators and staff of that agency. Guards agency internals (details with owner contacts, branches, staff lists) that customers and other roles must not read |

## Functions

### `User currentUserOrNull()`

**Purpose:** The signed-in, active user, or `null` for anonymous requests.

**Runs in:** read-only transaction

### `User requireCurrentUser()`

### `static boolean isAdmin(User user)`

### `static boolean isCustomer(User user)`

### `static boolean isAgencyStaff(User user)`

### `static boolean isBranchStaff(User user)`

**Purpose:** Managers and employees, whose tour lists are narrowed to their branch.

### `static boolean isSupportStaff(User user)`

### `static Integer agencyScope(User user)`

**Purpose:** Agency id that limits what this user may see; `null` means no agency limit.

### `void requireSelfOrAdmin(Integer userId)`

**Purpose:** Allows the account owner and administrators.

### `void requireRecordAccess(User current, Integer ownerId, Agency agency)`

**Purpose:** Customers may only touch their own records; agency staff only their agency's records.

### `void requireAgencyMember(User current, Agency agency)`

**Purpose:** Stricter than `#requireAgencyAccess`: only administrators and staff of this agency pass. Used for agency internals (branches, staff lists, owner contacts) that customers and other roles must not read.

### `void requireAgencyAccess(User current, Agency agency)`

**Purpose:** Agency staff may only act inside their own agency; other staff roles are not agency-bound.
