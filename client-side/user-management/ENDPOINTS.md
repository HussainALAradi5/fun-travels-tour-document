# User and Authentication Management Client API Usage Endpoints

This table is the feature-owned HTTP contract. Business rules and exception details are documented in this folder's service pages.

| ID | Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|---|
| EP-1 | `POST` | `/api/auth/register` | Create a customer account. | Validated `User` body | `UserService` | `createUser` |
| EP-2 | `POST` | `/api/auth/login` | Authenticate and issue a JWT. | Email/identifier and password map | `AuthService`, `UserService`, `JwtService` | `authenticate`, `login`, `generateToken` |
| EP-3 | `GET` | `/api/users` | List users for administration. | None | `UserService` | Repository-backed user listing |
| EP-4 | `GET` | `/api/users/{id}` | View one user. | User ID | `UserService` | `getUserById` |
| EP-5 | `GET` | `/api/users/agency/{agencyId}` | List agency staff, optionally by role. | Agency ID, optional `type` | `UserService` | `getAgencyUsers` |
| EP-6 | `PUT` | `/api/users/{id}` | Update a user profile. | User ID and validated `User` | `UserService` | `updateUser` |
| EP-7 | `POST` | `/api/users/bulk-import` | Import multiple employees. | Multipart file and `agencyId` | `UserService` | `bulkImportEmployees` |
| EP-8 | `PUT` | `/api/users/permissions/{id}` | Change role and branch assignment. | User ID, `type`, optional `branchId` | `UserService` | `updatePermissions` |
| EP-9 | `POST` | `/api/users/add-employee` | Create an employee account. | Validated `User` | `UserService` | `createUser` |
| EP-10 | `DELETE` | `/api/users/{id}` | Deactivate a user without deleting history. | User ID | `UserService` | `softDeleteUser` |
| EP-11 | `GET` | `/api/users/role/{type}` | Find users by application role. | `UserTypeEnum` | `UserService` | `getUsersByType` |
| EP-12 | `POST` | `/api/users/request-password-reset` | Send a reset link. | Email and base URL | `UserService` | `requestPasswordReset` |
| EP-13 | `POST` | `/api/users/confirm-password-reset` | Consume a reset token and set a password. | Identifier, token, base number, new password | `UserService` | `confirmPasswordReset` |
| EP-14 | `GET` | `/api/accounts/user/{userId}/balance` | Show wallet/account balance. | User ID | `AccountService` | `getAccountByUserId` |
| EP-15 | `GET` | `/api/accounts/user/{userId}/history` | Show wallet transaction history. | User ID | `AccountService` | `getTransactionHistory` |

## Endpoint rules

- Authentication and role authorization are enforced by the server.
- Request validation occurs before business-state changes.
- Success and error responses use the shared API envelope.
- Collection endpoints use bounded pagination where supported.

