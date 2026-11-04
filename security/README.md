# Security review

Review of the server, web client, and their contract (2026-11). Every finding below was fixed and is covered by a unit test or the end-to-end suite in [verification](../verification/README.md).

## Findings fixed

| # | Severity | Finding | Fix |
| --- | --- | --- | --- |
| 1 | Critical | JWTs were signed with a hard-coded key in source; anyone could forge an admin token | Key from `jwt.secret` (min 32 chars, validated at startup) |
| 2 | Critical | `PUT /api/users/{id}` accepted the whole `User` entity from any signed-in user, including `userType` (self-promotion to ADMIN) | `UserUpdateRequest` DTO, self-or-admin only, role never changes there |
| 3 | High | Any signed-in user could create agencies and branches | Agencies: admin only; branches: admin or owner of the agency |
| 4 | High | Owners/managers could create ADMIN accounts via add-employee and bulk import; bulk import accepted any agency | Role allow-lists per creator; imports limited to MANAGER/EMPLOYEE in the actor's agency |
| 5 | High | IDOR: wallets, notifications, payments, transactions, timelines, user profiles readable by any user | Ownership checks in `AccessPolicyService` |
| 6 | High | Agency staff saw and changed other agencies' reservations, tickets, payments, tours, fleet, meals | Agency scoping on every list and change |
| 7 | High | A reservation sent without tickets was priced at 0 and could be paid "in full" by wallet | Server always issues tickets and prices them |
| 8 | High | Cancelling a reservation after cancelling one ticket refunded that ticket twice; agency tour cancellation did the same | Refunds only cover still-active tickets |
| 9 | High | Releasing a reservation reset seats of already-cancelled tickets, even if resold (double booking) | Seats are derived per tour from active tickets |
| 10 | Medium | Password reset parameters (including the new password) were sent in the URL; reset revealed whether an email exists; links pointed to a dead port | JSON body, uniform response, link from `app.client-url`, new `/reset-password` page |
| 11 | Medium | Profile upload stored any bytes as `.jpg` | JPEG/PNG magic-byte check and size limit |
| 12 | Medium | CORS `*` on controllers and WebSocket | Single configured origin list |
| 13 | Medium | Unknown runtime errors returned raw exception messages (database details) | Generic 500 message, details logged |
| 14 | Low | Seed used a fixed `123456` password and logged it | Env/generated password, refuses `prod` |
| 15 | High | Tour, vehicle, seat, city, country, and port endpoints still bound request bodies straight to JPA entities (mass assignment, unchecked city/country pairs) | Dedicated request DTOs (`TourUpdateRequest`, `TransportationUpdateRequest`, `SeatUpdateRequest`, `CityCreateRequest`, `CountryCreateRequest`, `PortCreateRequest`) with validation |
| 16 | Medium | WebSocket notifications accepted unauthenticated connections and any topic | STOMP `CONNECT` requires a valid JWT; users may only subscribe to their own `/topic/notifications/<id>` (`WebSocketAuthInterceptor`) |
| 17 | Low | Booking requests sent travelers' passport numbers, birth dates, and contact details the server never used | Client sends only tour and ticket selections |

## Known limitations

- **Card and PayPal booking payments** stay PENDING: no signed provider webhook exists yet to complete them. Wallet payments work end to end. Wallet top-up uses Stripe Charges and was not exercised against Stripe.
- **Email delivery** for password reset was not exercised against an SMTP server.
- **Web client tokens** are stored in `localStorage` (readable by any script injected into the page); an httpOnly cookie session would be stronger.
- **Schema changes** rely on `ddl-auto=update` plus `SchemaMaintenance`; there are no versioned migrations yet.
