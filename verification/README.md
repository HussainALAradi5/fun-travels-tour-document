# Verification (2026-11-03)

| Repository | Check | Result |
| --- | --- | --- |
| Server | `./mvnw clean package` (43 unit tests, including WebSocket authentication; pricing, refunds, workflow transitions, pagination, codes, access policy, booking lifecycle, per-tour seats, entity equality) | Pass |
| Server | Runtime against PostgreSQL 18 (temporary cluster), seeded, 48-check end-to-end API suite: sign-in for every role, forged-token rejection, privilege escalation, IDOR, agency scoping, tour lifecycle, server-side pricing, wallet payment, single-ticket and reservation refunds without double refund, inventory release, per-tour seat sharing, meal rules, seat locks | 48/48 |
| Server | `SchemaMaintenance` against a database holding the legacy `tickets.seat_id` unique key | Constraint dropped, start continued |
| Web client | `tsc --noEmit`, `eslint src`, `next build` | Pass |
| Mobile | `tsc --noEmit`, `expo lint` (0 errors), `expo export --platform android` | Pass |
| Mobile | 20-check contract run of every endpoint the app calls, in app order | 20/20 |
| Server | Live STOMP checks with the client's own library: no token, invalid token, own topic, another user's topic | 4/4 |
| Server | Live checks for the new request DTOs (country/city/port validation, partial tour update without a vehicle, ignored forbidden fields) | 7/7 |
| Web client | After restructuring (services by domain, endpoint map, kebab-case folders, all components/hooks <= 150 lines): `tsc`, `eslint`, `next build` | Pass |
| Mobile | `expo lint` | 0 problems |
| Web client | Browser run of the production build (`next start`) against the live API (2026-11-04). Customer: catalog, sign-in, profile and wallet, reserve with per-tour seat picker and tour meals, wallet payment, My Bookings (travel dates, sorting, expired hold shown as cancelled), notifications. Admin: tours list and tour console (metrics, itinerary, seat manager, manifest, audit log), fleet, agencies and agency detail, users, meals, countries, ledger, requests. Notification WebSocket connects | Pass after the fixes below |

## Not verified

- Mobile screens on a device or emulator (no AVD/simulator available).
- Web client create/edit forms that write data (create tour, register vehicle, add agency/branch, seat configuration save) were opened but not submitted in the browser; their API calls are covered by the end-to-end suite.
- Stripe card top-up, card/PayPal booking payment completion, SMTP email delivery, and the content of WebSocket pushes (connection rules were verified).
