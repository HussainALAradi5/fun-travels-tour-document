# UserController

Base path `/api/users`. Source: `controllers/user/UserController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/users/me/profile` | `ProfileService.getMyProfile` | The signed-in user's profile with agency placement and wallet. | any signed-in user | - | `ProfileResponse` |
| `PUT /api/users/me/profile` | `ProfileService.updateMyProfile` | Name, mobile number, age, and profile image; role, agency, email, and password change elsewhere. | any signed-in user | body `UserUpdateRequest` | `ProfileResponse` |
| `GET /api/users` | `UserService.getUsersByType` | Admins see every active user. | ADMIN, MANAGER | - | `List<UserResponse>` |
| `GET /api/users/{id}` | `UserService.getVisibleUser` | Self, or any non-customer role (staff need to look up the customers they serve). | any signed-in user | - | `UserResponse` |
| `GET /api/users/agency/{agencyId}` | `UserService.getAgencyUsers` | Agency members are visible to admins and to staff of that agency. | any signed-in user | query `role` | `List<UserResponse>` |
| `PUT /api/users/{id}` | `UserService.updateProfile` | Users edit their own profile; admins edit anyone. | any signed-in user | body `UserUpdateRequest` | `UserResponse` |
| `POST /api/users/bulk-import` | `UserService.bulkImportEmployees` | Imports staff rows: username, name, email, password, age, mobile, role, branch name. | ADMIN, OWNER, MANAGER | query `file`, `agencyId` | `ImportResult` |
| `PUT /api/users/permissions/{id}` | `UserService.updatePermissions` | Admin-only role and placement change. | ADMIN | query `type`, `agencyId`, `branchId` | `UserResponse` |
| `POST /api/users/add-employee` | `UserService.createEmployee` | Admins create any staff role. | ADMIN, OWNER, MANAGER | body `EmployeeCreateRequest`; query `agencyId`, `branchId` | `UserResponse` |
| `DELETE /api/users/{id}` | `UserService.softDeleteUser` | Delete user. | ADMIN | - | `Void` |
| `GET /api/users/role/{type}` | `UserService.getUsersByType` | Admins see every active user. | ADMIN, MANAGER, OWNER | - | `List<UserResponse>` |
