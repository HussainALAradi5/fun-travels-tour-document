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

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Your account is inactive or no longer exists. | `AccessDeniedException` | 403 |

### `User requireCurrentUser()`

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Sign in to continue. | `AccessDeniedException` | 403 |
| Your account is inactive or no longer exists. | `AccessDeniedException` | 403 |

### `static boolean isAdmin(User user)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `static boolean isCustomer(User user)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `static boolean isAgencyStaff(User user)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `static boolean isBranchStaff(User user)`

**Purpose:** Managers and employees, whose tour lists are narrowed to their branch.

**Exceptions:** none of its own; failures come from the functions it calls.

### `static boolean isSupportStaff(User user)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `static Integer agencyScope(User user)`

**Purpose:** Agency id that limits what this user may see; `null` means no agency limit.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Your staff account is not linked to an agency. | `AccessDeniedException` | 403 |

### `void requireSelfOrAdmin(Integer userId)`

**Purpose:** Allows the account owner and administrators.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| You can only access your own account. | `AccessDeniedException` | 403 |
| Sign in to continue. | `AccessDeniedException` | 403 |
| Your account is inactive or no longer exists. | `AccessDeniedException` | 403 |

### `void requireRecordAccess(User current, Integer ownerId, Agency agency)`

**Purpose:** Customers may only touch their own records; agency staff only their agency's records.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| You are not allowed to access this record. | `AccessDeniedException` | 403 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| This record belongs to another agency. | `AccessDeniedException` | 403 |
| Your staff account is not linked to an agency. | `AccessDeniedException` | 403 |

### `void requireAgencyMember(User current, Agency agency)`

**Purpose:** Stricter than `#requireAgencyAccess`: only administrators and staff of this agency pass. Used for agency internals (branches, staff lists, owner contacts) that customers and other roles must not read.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Only this agency's staff can see its details. | `AccessDeniedException` | 403 |

### `void requireAgencyAccess(User current, Agency agency)`

**Purpose:** Agency staff may only act inside their own agency; other staff roles are not agency-bound.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| This record belongs to another agency. | `AccessDeniedException` | 403 |
| Your staff account is not linked to an agency. | `AccessDeniedException` | 403 |
