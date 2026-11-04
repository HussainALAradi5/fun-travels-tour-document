# Verification

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
