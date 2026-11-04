## Business logic

- `register` always creates a CUSTOMER. The mobile number must include the country code (`+97339990001`); spaces, dashes, brackets, and a leading `00` are removed first.
- `login` needs a password and accepts an email, a username, or a mobile number in any common format (`+973 3999 0001`, `0097339990001`, `97339990001`); `UserRepository.findByLoginIdentifier` is the one lookup used by sign-in and by Spring Security. Wrong credentials return 401; deactivated accounts 403.
- `requestPasswordReset` answers the same way whether or not the email exists, stores a random token valid for 15 minutes, and emails `<app.client-url>/reset-password?token=...&email=...`.
- `confirmPasswordReset` compares the token in constant time, rejects expired or wrong tokens (409 `INVALID_RESET_LINK`), and clears the token after use.
