# UserController

Base path `/api/v1/users`. Source: `controllers/user/UserController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/v1/users/me/profile` | `ProfileService.getMyProfile` | The signed-in user's profile with agency placement and wallet. | any signed-in user | - | `ProfileResponse` | 401, 403 |
| `PUT /api/v1/users/me/profile` | `ProfileService.updateMyProfile` | Name, mobile number, age, and profile image; role, agency, email, and password change elsewhere. | any signed-in user | body `UserUpdateRequest` | `ProfileResponse` | 400, 401, 403 |
| `GET /api/v1/users` | `UserService.getUsersByType` | Admins see every active user. | ADMIN, MANAGER | - | `List<UserResponse>` | 401, 403 |
| `GET /api/v1/users/{id}` | `UserService.getVisibleUser` | Self, or any non-customer role (staff need to look up the customers they serve). | any signed-in user | - | `UserResponse` | 401, 403, 404 |
| `GET /api/v1/users/agency/{agencyId}` | `UserService.getAgencyUsers` | Agency members are visible to admins and to staff of that agency. | any signed-in user | query `role` | `List<UserResponse>` | 400, 401, 403, 404 |
| `PUT /api/v1/users/{id}` | `UserService.updateProfile` | Users edit their own profile; admins edit anyone. | any signed-in user | body `UserUpdateRequest` | `UserResponse` | 400, 401, 403, 404, 409 |
| `POST /api/v1/users/bulk-import` | `UserService.bulkImportEmployees` | Imports staff rows: username, name, email, password, age, mobile, role, branch name. | ADMIN, OWNER, MANAGER | query `file`, `agencyId` | `ImportResult` | 400, 401, 403, 404, 409 |
| `PUT /api/v1/users/permissions/{id}` | `UserService.updatePermissions` | Admin-only role and placement change. | ADMIN | query `type`, `agencyId`, `branchId` | `UserResponse` | 400, 401, 403, 404 |
| `POST /api/v1/users/add-employee` | `UserService.createEmployee` | Admins create any staff role. | ADMIN, OWNER, MANAGER | body `EmployeeCreateRequest`; query `agencyId`, `branchId` | `UserResponse` | 400, 401, 403, 404, 409 |
| `DELETE /api/v1/users/{id}` | `UserService.softDeleteUser` | Delete user. | ADMIN | - | `Void` | 400, 401, 403, 404 |
| `GET /api/v1/users/role/{type}` | `UserService.getUsersByType` | Admins see every active user. | ADMIN, MANAGER, OWNER | - | `List<UserResponse>` | 401, 403 |
