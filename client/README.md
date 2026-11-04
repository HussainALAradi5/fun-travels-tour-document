# Web client

Next.js App Router with Chakra UI. Layers under `src/`:

| Folder | Role |
| --- | --- |
| `app/` | Routes only; each page renders a page component |
| `components/pages/` | Page-level containers composed by routes (`components/pages/tour-management/...`) |
| `components/` | Reusable and domain UI |
| `hooks/` | State and data loading |
| `services/<domain>/` | Typed services named after their export (`services/user/userService.ts`) over one axios client (`config/BaseApi.ts`) |
| `config/` | `api.config.ts` (API base URL, origin, WebSocket URL from `NEXT_PUBLIC_*`) and `endpoints.ts` (every API path, mirroring the server controllers) |
| `dtos/<domain>/` | Generated mirrors of the server DTOs (`TourResponseDto`, `RegisterRequestDto`, ...). Services send and receive these; do not edit by hand |
| `interfaces/`, `types/`, `enums/` | Read models (aliases of DTOs, for example `type Tour = TourResponseDto`), form and UI types, enums - one per file |
| `utilities/` | Pure helpers, auth and notification contexts |

## Contract changes in this release

| Area | Change |
| --- | --- |
| Profile | `updateUser` sends `UserUpdateRequest` (`name`, `mobileNumber`, `age`, `base64Image`, `removeImage`) |
| Staff | `addEmployee(EmployeeCreateRequest, agencyId?, branchId?)`; `bulkImport` returns `ImportResult` |
| Password reset | `POST /auth/password-reset/request` and `/confirm` with JSON bodies; new `/reset-password` page |
| Booking | Seat picker asks `/seats/search?tourId=` for per-tour availability; meals come from `tour.availableMeals` |
| Notifications | WebSocket count reads `unreadCount` (was `unread`, always undefined) |

## Fixed client defects

- Bulk-import template had Name and Username in the wrong order for the server parser.
- `getAllBranches` called `/api/api/branches`; `getVisibleStaff` called a non-existent endpoint (removed).
- Profile image and WebSocket URLs were hard-coded to `localhost:8080`.
- The booking page offered every meal in the system instead of the tour's meals.
- Unused `useBookingCheckout` path (created zero-priced bookings) is no longer reachable on the server.

## More defects fixed during the 150-line split

| Area | Defect | Fix |
| --- | --- | --- |
| Mobile number field | Re-fetched the whole country list on every keystroke and reset the selection | Countries load once |
| Add branch | Manager sent as `branchManager` (server reads `branchManagerId`), so managers were never assigned; contact sent as `ownerMobileNumber`; country/city asked although the API has none | Payload mirrors `AgencyBranchCreateRequest`; manager list limited to MANAGER users |
| Add agency | Owner list showed every user (server requires OWNER); contact number had no field | OWNER users only; field added |
| Tour edit | A tour without a vehicle sent `{ id: 0 }` and failed with "Transportation not found" | Only set references are sent |
| Notifications | Reservation links opened the ticket page with a reservation id; customers were sent to admin tour pages | Role-aware routes |
| Wallet top-up | Offered bank transfer, which the server rejects; debug logs; inaccurate "256-bit" claim | Card only; accurate Stripe notice |
| Fleet table | "Utilization" read a vehicle-level seat count that no longer changes (seats are per tour) | Shows capacity |
| Booking | Sent guests' passport and birth data the server never used | Only selections sent |
| City admin | Delete confirmation had no text; icon buttons had no accessible names | Named city in dialog; `aria-label`s |
| Users admin | Role filter missing OWNER | Added |
| Comments | "Edited" marker never shown (server never sent `updatedAt`) | Server now sends it when a comment was edited |

## Defects fixed during the browser test (2026-11-04)

| Area | Defect | Fix |
| --- | --- | --- |
| Tour catalog | Country names and flags blank (server sent only `famousName`) | Server sends `officialName`, `flagPngUrl`, destinations |
| My Bookings | Travel date "TBD" for every ticket | Server sends tour dates on tickets |
| Seat picker and seat manager | Seats in text order `S1, S10, S2` | `SEAT_ORDER` (`id` ascending) |
| Tour console | Revenue counted cancelled tickets at base price; vehicle shown as "TR-UNASSIGNED"; header said "Reservation - Step 1" | Live tickets at their paid price; `transportationNumber`; status and tour number |
| Agencies, branches, itinerary | "City, Country" printed ", " when unset | `formatPlace` |

## Defects found by switching to generated DTOs (2026-11-04)

| Area | Defect | Fix |
| --- | --- | --- |
| Boarding pass, journey tracker, verification | Read the tour's cities, countries, vehicle, and status from the ticket, which only carries a tour summary, so they always showed TBD | `useTicketDetail` also loads the tour |
| Agency detail | Branches tab read `agency.branches`, which the server never sends, so it was always empty | Loads `GET /branches/agency/{id}` |
| Branch table and export | Showed city, country, and owner mobile, which branches do not have | Shows contact number and manager |
| Profile edit | Offered "New password" and "Image URL", which the server ignores; had no name field | Name added; ignored fields removed; page uses `/users/me/profile` |
| Register, add employee, agency contacts | Plain text phone fields; numbers could miss the country code | Country-code picker (`mobile` field type) |
| Meals | No edit or activate/deactivate; logic inside the page component | `useMealPlans`, `useMealPlanColumns`, row actions |
| Card top-up | Logged the Stripe token and each step; offered non-card text | Card-only form; logic in `useCardTopUp` |
| Ticket | `Ticket.isPaid` read a field the server never sends (`paid`) | Ticket is the DTO |

## Structure change

`features/` moved to `components/pages/`, `Api/` to `services/`, and `interface/` to `interfaces/` (moved with git history; 268 import paths rewritten). Every component, page, and hook file is at most 150 lines: logic lives in hooks (`hooks/<domain>/`), field and column definitions in `constants/` or column hooks, and repeated markup in child components. All folders under `src/` (except Next.js route segments such as `[tourId]`) use kebab-case: `components/tour-management/seat/seat-management`, `components/ui/custom/dialogs`, `hooks/tour-management`, `services/agency`. Component files keep PascalCase (`SeatManager.tsx`), hooks keep camelCase (`useTourManagement.ts`), and service files keep their current names (`services/User.ts`). 43 folders were renamed with git and their imports rewritten.
