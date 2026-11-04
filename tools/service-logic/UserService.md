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
