# ProfileService

Source: `services/user/ProfileService.java`.

The signed-in user's own profile: identity, placement, and wallet in one view.

## Business logic

The signed-in user's own profile in one response (`ProfileResponse`): identity, contact, role, agency and branch, wallet, and membership date. `getMyProfile` opens a wallet for older accounts that have none. `updateMyProfile` applies the same rules as `UserService.updateProfile` to the current user and returns the refreshed profile.

## Functions

### `ProfileResponse getMyProfile()`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `ProfileResponse updateMyProfile(UserUpdateRequest request)`

**Purpose:** Name, mobile number, age, and profile image; role, agency, email, and password change elsewhere.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
