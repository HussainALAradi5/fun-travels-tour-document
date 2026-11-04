## Business logic

- `register` always creates a CUSTOMER.
- `login` accepts email, username, or mobile. Wrong credentials return 401; deactivated accounts 403.
- `requestPasswordReset` answers the same way whether or not the email exists, stores a random token valid for 15 minutes, and emails `<app.client-url>/reset-password?token=...&email=...`.
- `confirmPasswordReset` compares the token in constant time, rejects expired or wrong tokens (409 `INVALID_RESET_LINK`), and clears the token after use.
