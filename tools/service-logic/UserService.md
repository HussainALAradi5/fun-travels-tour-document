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
