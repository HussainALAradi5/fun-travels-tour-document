# Security model

- **Authentication.** `JwtAuthenticationFilter` (in `middlewares/`) reads `Authorization: Bearer <token>`. Tokens are HS256-signed with `jwt.secret` and expire after `jwt.expiration`. Missing or invalid tokens on protected routes return **401** (`HttpStatusEntryPoint`).
- **Public routes.** `POST /api/auth/**`; `GET` on `/api/tours/**`, `/api/meals/**`, `/api/countries/**`, `/api/cities/**`, `/api/ports/**`, `/api/wallet/config`, `/uploads/**`; the WebSocket handshake.
- **Role checks.** `@PreAuthorize` on controllers and services, plus URL rules for `/api/tickets/**`, `/api/reservations/**`, `/api/notifications/**` (customer and agency roles).
- **Ownership and tenancy.** [AccessPolicyService](../services/auth/AccessPolicyService.md): customers reach only their own records; agency staff only their agency's records; admins everything.
- **WebSocket.** `/ws-notifications` handshakes are open, but STOMP `CONNECT` must carry `Authorization: Bearer <token>` and a user may subscribe only to `/topic/notifications/<their id>`.
- **Headers.** `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`; CORS limited to `app.cors-allowed-origins`.
- **Passwords.** BCrypt. Reset tokens expire after 15 minutes and are compared in constant time.

See [security review](../../security/README.md) for findings and limitations.
