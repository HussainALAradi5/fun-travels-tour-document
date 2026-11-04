# Account use cases

## UC-AU-01 Visitor registers

- **Main flow:** `POST /api/auth/register` with username, name, email, password (6+), international mobile -> CUSTOMER account and wallet created -> sign in.
- **Failure flows:** Duplicate email, username, or mobile -> 409; invalid fields -> 400 with `fieldErrors`.

## UC-AU-02 User resets a password

- **Main flow:** `POST /api/auth/password-reset/request` -> same answer for any email; if the account exists, a 15-minute link to `/reset-password?token&email` is emailed -> user sets a new password -> `POST /api/auth/password-reset/confirm`.
- **Failure flows:** Wrong or expired token -> 409 `INVALID_RESET_LINK`.

## UC-AU-03 Owner adds staff

- **Main flow:** `POST /api/users/add-employee` with `EmployeeCreateRequest` -> account created in the owner's agency.
- **Failure flows:** Owner assigns ADMIN, OWNER, or another non-allowed role -> 403; branch of another agency -> 400.
