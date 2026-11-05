# Verification

## 2026-11-06: gender, keyboard, demo catalog

| Repository | Check | Result |
| --- | --- | --- |
| Server | `./mvnw package` (unit tests) | Pass |
| Server | Fresh database, every live suite with gender sent on sign-up and staff creation: 48 + 20 + 37 + 24 + 32 + 52 + 4 + 53 + 36 | 306/306 |
| Server | `gender_check`: sign-up without or with an invalid gender refused, FEMALE stored and returned, profile shows it, user changes it, other edits keep it, staff need it, staff lists and seeded accounts have it | 10/10 |
| Server | Demo catalog on a fresh database: 4 tours listed; a family of 2 adults and 2 kids with a meal each on the Muscat sale tour costs 1226 | Pass |
| Web | At 412 px: sign-up with Female, stored as FEMALE; profile shows the pink Female badge; Edit Profile opens with Female chosen; typecheck, lint, build | Pass |
| Mobile | Typecheck, lint | Pass |
| Not verified | The mobile keyboard fix and gender screens on a phone | - |

## 2026-11-05 (night): business rules and family booking

| Repository | Check | Result |
| --- | --- | --- |
| Server | `./mvnw package`: 88 unit tests (adds policy pricing and refunds, country directory, dial codes) | Pass |
| All | Fresh database: end-to-end 48, booking contract 20, earlier round 37, mobile screens 24, access 32, reports 52, WebSocket 4 | 217/217 |
| Server | `business_check`: pricing (adult, kids chair, premium seat with a meal, mixed booking of 3), client prices ignored, automatic seats, duplicate/taken seats, capacity, holds, overlapping dates, inactive tours, refunds at 30/10/3 days and 20/35 days under a custom policy, refund quotes equal refunds and are private, agency cancellation limits, tour workflow, policy permissions and validation | 53/53 |
| Server | `rules_check`: meals (diet rules, not offered, inactive, price change after payment), seats in maintenance, hold expiry returning places and seats, double payment, vehicle capacity and layout lock, overlapping vehicle tours, capacity below bookings, dates, sale price, staff roles | 36/36 |
| Web | Booking page with 2 adults and 2 children, seated in one click: estimate $300 ($400 - $100 kids); server charged $300 with 4 tickets; ticket page shows the journey and "Cancel now and $50.00 of $50.00 (100%) returns" | Pass |
| Web | `typecheck`, `lint`, `build` | Pass |
| Mobile | `typecheck`, `lint` | Pass |
| Not verified | The new mobile booking screen on the phone (hot-reloaded, not yet tapped through) | - |

## 2026-11-05 (evening): review fixes

| Repository | Check | Result |
| --- | --- | --- |
| Server | `./mvnw package`: 79 tests (adds error mapping, auth rate limit, nightly job transactions) | Pass |
| Server | Flyway on an empty database: V1 and V2 applied, schema validated, seed ran | Pass |
| Server | Flyway on a database built by Hibernate with the retired column and seat constraint added back | Baselined at 1, V2 applied, both dropped, 54 indexes |
| All | Fresh database after each fix (errors, migrations, lazy loading, middleware, `/api/v1`, layer move): end-to-end 48/48, booking contract 20/20, earlier round 37/37, mobile screens 24/24, access and logic 32/32, reports 52/52, WebSocket 4/4 | 217/217 each time |
| Server | Rate limit at 3 per window: fourth login gets 429 `TOO_MANY_REQUESTS` with `Retry-After: 60`; `X-Request-Id` echoed and in the log; DELETE on a POST route gets 405 | Pass |
| Server | SQL statements per list request, same data, before and after lazy loading | agencies 8 to 4, branches 5 to 3, tours 18 to 10, tickets 17 to 6, reservations 14 to 5, requests 5 to 3, vehicles 7 to 4, users 19 to 5, catalog 12 to 7, customer tickets 9 to 5 |
| Web | `npm run typecheck`, `npm run lint`, `npm run build` | Pass |
| Mobile | `npm run typecheck`, `npm run lint` | Pass |
| Not verified | Mobile on an emulator or device; nightly jobs at midnight (covered by a unit test) | - |

## 2026-11-05: code cleanup

| Repository | Check | Result |
| --- | --- | --- |
| Server | `./mvnw test` | 69/69 |
| All | Fresh database after the service split: end-to-end 48/48, booking contract 20/20, earlier round 37/37, mobile screens 24/24, access and logic 32/32, reports 52/52, WebSocket 4/4 | 217/217 |
| Clients | DTOs regenerated (no `MediaFileDto`); web `tsc` and `eslint`, mobile `tsc` and `expo lint` | Pass |

## 2026-11-04 (late night): access and logic fixes

| Repository | Check | Result |
| --- | --- | --- |
| Server | `./mvnw test`: 69 tests (adds place recount, drift correction, nightly reconciliation, report retention) | Pass |
| Server | Start-up against a database holding the old `tours.price` and `transportations.remaining_seats` columns | Both dropped, start continued |
| Server | 32 live access and logic checks: customer/owner/manager/employee/admin access to agencies, branches, and staff; cross-agency reads refused; manager transfer refused; tour visibility for visitors, customers, ticket holders, staff, and admins; places counted from tickets on booking and cancellation; vehicle responses without counters | 32/32 |
| All | Regression on a fresh database: end-to-end 48/48, booking contract 20/20, earlier round 37/37, mobile screens 24/24, reports 52/52, WebSocket 4/4 | Pass |
| Clients | DTOs regenerated; web `tsc` and `eslint`, mobile `tsc` | Pass |

## 2026-11-04 (late): mobile parity

| Repository | Check | Result |
| --- | --- | --- |
| Mobile | `tsc --noEmit`, `expo lint` (0 problems), `expo export --platform android`; every screen at most 150 lines | Pass |
| Mobile | Contract run of every endpoint the new screens call, in app order, against a running server | 24/24, plus payment detail on a paid booking |
| Mobile | Original booking contract run | 20/20 |
| Not verified | The app on an Android or iOS device or emulator (none available); the share sheet and photo picker need a device | - |

## 2026-11-04 (night): server-generated reports

| Repository | Check | Result |
| --- | --- | --- |
| Server | `./mvnw test`: 65 tests, including PDF text checks (letterhead, meta, every row, "Page x of y") and Excel structure (header row, typed dates and money, frozen pane, footer) | Pass |
| Server | Live: every report type in PDF and Excel as the allowed role, downloaded and checked by file signature; customer/employee role limits; missing parameters; sign-in required; download and delete limited to the owner or an admin; storage path never returned | 52/52 |
| Web client | `tsc`, `eslint`, `next build`; browser: admin Export -> PDF on the tour inventory made `POST /api/reports` (201) and `GET /api/media/{id}/download` (200) and saved the server's file | Pass |

## 2026-11-04 (later): DTO records, sign-in, profile, review fixes

| Repository | Check | Result |
| --- | --- | --- |
| Server | `./mvnw clean package`: 60 unit tests (adds `MobileNumbersTest`) | Pass |
| Server | Fresh PostgreSQL database, seeded; 48-check end-to-end API suite | 48/48 |
| Server | 37 live checks for this round: sign-in by email, username, and phone in five formats; blank and wrong password; registration without country code rejected and with spaces accepted; `GET`/`PUT /users/me/profile`; wire names after the record change (`paid`, tour dates); public meal list, meal edit and permissions; fleet scoping and search; manager/owner user lists; per-tour seat filters and totals; card booking payment rejected; 404s; admin role change rules | 37/37 |
| Server | Live STOMP checks | 4/4 |
| Web client | `tsc --noEmit`, `eslint src`, `next build`; every `.tsx` at most 150 lines | Pass |
| Web client | Browser, production build: sign-in by phone with spaces; profile page (member since, wallet account) and profile edit save; ticket boarding pass shows route and vehicle; register shows the +973 picker; meals edit, activate, deactivate; agency Branches tab lists branches | Pass |
| Mobile | `tsc --noEmit`, `expo lint`, `expo export --platform android`; 20-check contract run | Pass, 20/20 |

## 2026-11-03

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
- Stripe card top-up against Stripe, SMTP email delivery, and the content of WebSocket pushes (connection rules were verified). Card and PayPal booking payments are now rejected by design.
- The mobile phone picker and profile tab were type-checked and bundled but not opened on a device.
