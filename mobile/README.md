# Mobile app

Expo SDK 58 (React Native 0.88) with Expo Router and TypeScript. It covers everything a customer does on the web app, against the same server API.

## Screens and their web counterparts

| Mobile | Web | Server calls |
| --- | --- | --- |
| Tours tab: catalog with from/to country and date filters, Export catalog | `/tours` | `GET /tours/catalog`, `GET /countries`, `POST /reports` |
| `tours/[id]`: details, seats, meals, travelers, book | `/reserve/[tourId]` | `GET /tours/{id}`, `GET /seats/search`, `POST /reservations` |
| Bookings tab, `bookings/[id]`: pay with wallet, cancel, Export my tickets | `/my-bookings`, `/my-bookings/[id]` | `/reservations`, `/payments/execute/{id}`, `/tickets/search` |
| `tickets/[id]`: boarding pass (route, countries, dates, seat, vehicle, passenger, paid/due, QR), cancel | ticket detail | `GET /tickets/{id}`, `GET /tours/{id}`, `PUT /tickets/{id}/cancel` |
| Wallet tab, `transactions/[id]`, `payments`, `payments/[id]`, Export ledger | `/transactions`, `/payments` | `/accounts/user/{id}/*`, `/transactions/{id}`, `/payments`, `/payments/{id}` |
| Alerts tab: tap opens the booking, ticket, tour, or request | `/my-notifications` | `/notifications/user/{id}`, `PUT /notifications/{id}/read` |
| `requests`, `requests/new`, `requests/[id]`: create, reply, delete while pending | `/my-requests` | `/user-requests`, `/tracking/USER_REQUEST/{id}[/comments]` |
| Profile tab, `profile/edit`: name, mobile with country code, age, photo | `/profile` | `GET`/`PUT /users/me/profile` |
| `reports`: open/share or delete PDF and Excel reports | Export buttons | `GET /media`, `GET /media/{id}/download`, `DELETE /media/{id}` |
| `(auth)` login, register, forgot password, reset with code | `/login`, `/register`, `/forgot-password`, `/reset-password` | `/auth/*` |

Card top-up stays on the web: Stripe card entry needs a native build, not Expo Go. Bookings are paid from the wallet on both.

## Layers (`src/`)

| Folder | Role |
| --- | --- |
| `app/` | Expo Router screens only; each renders and takes its state from a hook |
| `config/` | `api.config.ts` (origin from `EXPO_PUBLIC_API_URL`), `endpoints.ts` (paths matching server routes) |
| `constants/` | Theme tokens (light/dark), messages, phone rules, limits |
| `enums/` | Server enums used by screens, and the status-to-color map |
| `dtos/<domain>/` | Generated mirrors of the server DTOs the app calls (`tools/generate-ts-dtos.py ... mobile`); do not edit by hand |
| `interfaces/` | Read models (aliases of the DTOs), props, and state - one per file |
| `services/` | `apiClient.ts` (base URL, bearer token, 15 s timeout, error mapping, 401 sign-out) and one service per area: auth, tours, bookings, tickets, payments, wallet, notifications, support, profile, countries, reports |
| `providers/`, `hooks/` | Auth session, data loading (`useAsync`), mutations (`useAction`), and one hook per screen |
| `components/` | Common (Button, TextField, Card, Chip, StateView, StatusBadge, Screen, SelectSheet, PhoneField, InfoRow, LinkRow, Avatar) and domain components (BoardingPass, TicketCard, CatalogFilters, ExportButton, ...) |
| `utilities/` | Formatting, errors, secure session storage, notification routes, authenticated download and share |

## Behavior

- Tokens are kept in `expo-secure-store` (Keychain/Keystore).
- Sign-in accepts an email, username, or mobile number. Phone fields use a searchable country-code picker (Bahrain by default) and send `+<code><number>`.
- Reports are built by the server from all of the user's records. The app downloads them with the user's token (`expo-file-system` `File.createDownloadTask`) and opens the share sheet (`expo-sharing`); files are never public links.
- Profile photos come from the photo library (`expo-image-picker`, square crop) and are sent as base64; the server stores them and returns the new path.
- Prices, seat availability, refunds, and permissions come from the server; the app only renders them.
- Destructive actions (cancel booking or ticket, delete request or report) ask for confirmation.
- Touch targets are at least 44 pt; screens are safe-area and keyboard aware; colors follow the system light/dark setting; every screen file is at most 150 lines.

## Verification

`tsc --noEmit` and `expo lint` pass with 0 problems, and `expo export --platform android` produces the bundle (2026-11-04). Against a running server: the original 20-check booking contract and 24 checks for the new screens (catalog filters, profile edit with photo and spaced phone, avatar URL, boarding pass fields, transaction detail, payments, support request create/reply/delete, report export and authenticated download for tickets, ledger, and catalog, report list and delete, reset with a wrong code, routable notifications), plus a paid booking to check payment detail fields. **Not yet run on an emulator or device**: no Android AVD or iOS simulator was available.
