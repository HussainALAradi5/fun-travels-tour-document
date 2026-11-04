# AuthController

Base path `/api/auth`. Source: `controllers/auth/AuthController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `POST /api/auth/register` | `AuthService.register` | Public sign-up always creates a customer account. | public | body `RegisterRequest` | `UserResponse` |
| `POST /api/auth/login` | `AuthService.login` | Accepts email, username, or mobile number; Spring Security verifies the password hash. | public | body `LoginRequest` | `AuthResponse` |
| `POST /api/auth/password-reset/request` | `AuthService.requestPasswordReset` | Request password reset. | public | body `PasswordResetRequest` | `String` |
| `POST /api/auth/password-reset/confirm` | `AuthService.confirmPasswordReset` | Confirm password reset. | public | body `PasswordResetConfirmRequest` | `UserResponse` |
