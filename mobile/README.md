# Mobile app

Expo SDK 58 (React Native 0.88) with Expo Router and TypeScript. Customer-focused: browse tours, book with optional seats and meals, pay by wallet, view tickets with QR codes, cancel, wallet history, notifications.

## Layers (`src/`)

| Folder | Role |
| --- | --- |
| `app/` | Expo Router screens only: `(auth)` login/register/forgot-password, `(tabs)` tours/bookings/wallet/notifications/profile, `tours/[id]`, `bookings/[id]` |
| `config/` | `api.config.ts` (origin from `EXPO_PUBLIC_API_URL`), `endpoints.ts` (paths matching server routes) |
| `constants/` | Theme tokens (light/dark), messages, limits |
| `enums/` | Status enums and the status-to-color map |
| `interfaces/` | Wire contracts mirroring server DTOs, props, and state - one per file |
| `services/` | `apiClient.ts` (base URL, bearer token, 15 s timeout, error mapping, 401 sign-out) and domain services |
| `providers/`, `hooks/` | Auth session, data loading, forms, actions |
| `components/` | Common (Button, TextField, Card, Chip, StateView, StatusBadge, Screen) and domain components |
| `utilities/` | Formatting, errors, secure session storage |

## Behavior

- Tokens are kept in `expo-secure-store` (Keychain/Keystore).
- Prices, seat availability, refunds, and permissions come from the server; the app only renders them.
- Destructive actions (cancel booking or ticket) ask for confirmation and show the refund policy.
- Touch targets are at least 44 pt; screens are safe-area and keyboard aware; colors follow the system light/dark setting.

## Verification

`tsc --noEmit` passes, `expo lint` has 0 errors (4 warnings for the shared `const` + `type` enum pattern), and `expo export --platform android` produces the bundle. Every endpoint the app calls was exercised against a running server (20/20 contract checks). **Not yet run on an emulator or device**: no Android AVD or iOS simulator was available.
