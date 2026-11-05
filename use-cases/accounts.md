# Account use cases

## UC-AU-01 Visitor registers

- **Main flow:** `POST /api/auth/register` with username, name, email, password (6+, with a show/hide button), gender (MALE or FEMALE), international mobile -> CUSTOMER account and wallet created -> sign in.
- **Failure flows:** Duplicate email, username, or mobile -> 409; invalid fields or no gender -> 400 with `fieldErrors`; a gender other than MALE or FEMALE -> 400.

## UC-AU-02 User resets a password

- **Main flow:** `POST /api/auth/password-reset/request` -> same answer for any email; if the account exists, a 15-minute link to `/reset-password?token&email` is emailed -> user sets a new password -> `POST /api/auth/password-reset/confirm`.
- **Failure flows:** Wrong or expired token -> 409 `INVALID_RESET_LINK`.

## UC-AU-03 Owner adds staff

- **Main flow:** `POST /api/users/add-employee` with `EmployeeCreateRequest` (gender required) -> account created in the owner's agency.
- **Failure flows:** Owner assigns ADMIN, OWNER, or another non-allowed role -> 403; branch of another agency -> 400.

## UC-AU-04 User sets their gender

- **Main flow:** Profile -> Edit -> Male or Female -> `PUT /api/users/{id}` with `gender` -> the profile, staff lists, the user directory and its report show a colored badge (blue with the male sign, pink with the female sign).
- **Notes:** Accounts created before gender was asked have none until they choose; no badge is shown for them. Leaving `gender` out of an update keeps the current value.
