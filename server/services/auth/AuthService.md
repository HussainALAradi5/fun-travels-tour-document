# AuthService

Source: `services/auth/AuthService.java`.

## Business logic

- `register` always creates a CUSTOMER.
- `login` accepts email, username, or mobile. Wrong credentials return 401; deactivated accounts 403.
- `requestPasswordReset` answers the same way whether or not the email exists, stores a random token valid for 15 minutes, and emails `<app.client-url>/reset-password?token=...&email=...`.
- `confirmPasswordReset` compares the token in constant time, rejects expired or wrong tokens (409 `INVALID_RESET_LINK`), and clears the token after use.

## Functions

### `User register(RegisterRequest request)`

**Purpose:** Public sign-up always creates a customer account.

**Runs in:** transaction

### `AuthResponse login(LoginRequest request)`

**Purpose:** Accepts email, username, or mobile number; Spring Security verifies the password hash.

**Runs in:** read-only transaction

### `String requestPasswordReset(String email)`

**Runs in:** transaction

### `User confirmPasswordReset(PasswordResetConfirmRequest request)`

**Runs in:** transaction
