## Business logic

The signed-in user's own profile in one response (`ProfileResponse`): identity, contact, role, agency and branch, wallet, and membership date. `getMyProfile` opens a wallet for older accounts that have none. `updateMyProfile` applies the same rules as `UserService.updateProfile` to the current user and returns the refreshed profile.
