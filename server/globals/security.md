# Security model

All REST paths sit under the configured prefix (`app.api-prefix`, default `/api`).

- **Authentication.** `middlewares/auth/JwtAuthenticationFilter` reads `Authorization: Bearer <token>`. Tokens are HS256-signed with `jwt.secret` and expire after `jwt.expiration`. Missing or invalid tokens on protected routes return **401** with the shared JSON envelope (`middlewares/errors/SecurityErrorResponder`, code `UNAUTHORIZED`); a role denied by a URL rule returns **403** (`FORBIDDEN`).
- **Rate limiting.** `middlewares/security/AuthRateLimitFilter` allows `app.rate-limit.auth-requests` (default 10) POSTs to `/api/auth/**` per client address and path in each `app.rate-limit.window-seconds` (default 60). Further attempts get **429** `TOO_MANY_REQUESTS` with `Retry-After`. Counts are in memory, so each server instance limits on its own; behind a proxy, configure it to pass the client address.
- **Request IDs.** `middlewares/logging/RequestIdFilter` accepts a safe `X-Request-Id` (8 to 64 letters, digits, `.`, `_`, `-`) or generates one, returns it in the response, adds it to every log line, and logs one line per API request with status and duration. Bodies, tokens and passwords are never logged.
- **Public routes.** `POST /api/auth/**`; `GET` on `/api/tours/**`, `/api/meals/**`, `/api/countries/**`, `/api/cities/**`, `/api/ports/**`, `/api/wallet/config`, `/uploads/**`; the WebSocket handshake.
- **Role checks.** `@PreAuthorize` on controllers and services, plus URL rules for `/api/tickets/**`, `/api/reservations/**`, `/api/notifications/**` (customer and agency roles).
- **Ownership and tenancy.** [AccessPolicyService](../services/auth/AccessPolicyService.md): customers reach only their own records; agency staff only their agency's records; admins everything.
- **WebSocket.** `/ws-notifications` handshakes are open, but STOMP `CONNECT` must carry `Authorization: Bearer <token>` and a user may subscribe only to `/topic/notifications/<their id>`.
- **Headers.** `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`; CORS limited to `app.cors-allowed-origins` and exposes `X-Request-Id` and `Retry-After`.
- **Passwords.** BCrypt. Reset tokens expire after 15 minutes and are compared in constant time.
- **Error details.** Storage and external-service failures are logged with their cause and returned with a generic message, so file paths and setting names never reach the caller.

See [security review](../../security/README.md) for findings and limitations.
