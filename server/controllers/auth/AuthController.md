# AuthController

Base path `/api/v1/auth`. Source: `controllers/auth/AuthController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /api/v1/auth/register` | `AuthService.register` | Public sign-up always creates a customer account. | public | body `RegisterRequest` | `UserResponse` | 400 |
| `POST /api/v1/auth/login` | `AuthService.login` | Accepts email, username, or mobile number; Spring Security verifies the password hash. | public | body `LoginRequest` | `AuthResponse` | 400, 409 (`INVALID_CREDENTIALS`) |
| `POST /api/v1/auth/password-reset/request` | `AuthService.requestPasswordReset` | Request password reset. | public | body `PasswordResetRequest` | `String` | 400 |
| `POST /api/v1/auth/password-reset/confirm` | `AuthService.confirmPasswordReset` | Confirm password reset. | public | body `PasswordResetConfirmRequest` | `UserResponse` | 400, 409 (`INVALID_RESET_LINK`) |
