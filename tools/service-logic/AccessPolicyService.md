## Business logic

Controllers check roles; this service checks whose data a signed-in user may touch.

| Rule | Behavior |
| --- | --- |
| `requireSelfOrAdmin(userId)` | Wallet, notifications, profile edits |
| `requireRecordAccess(user, ownerId, agency)` | Customers: only their own record. Agency staff (OWNER, MANAGER, EMPLOYEE): only their agency. Admin and support: unrestricted |
| `agencyScope(user)` | Agency id applied to list queries for agency staff; staff without an agency are rejected |
| `requireAgencyMember(user, agency)` | Stricter: only administrators and staff of that agency. Guards agency internals (details with owner contacts, branches, staff lists) that customers and other roles must not read |
