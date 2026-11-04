# Implementation Updates

## 2026-11-04 (late night) - Access and logic fixes

- **Access.** Agency details, staff lists, branches, and agency search are limited to administrators and the agency's own staff; owners can no longer pull another agency's manager into a branch; only bookable tours are public. See [security](security/README.md) items 26-30.
- **Places.** Available places are counted from the tour's tickets at every booking and reconciled nightly, instead of trusting a stored counter.
- **Reports.** Generated reports are deleted nightly after `app.report-retention-days` (`REPORT_RETENTION_DAYS`, default 30).
- **Model.** Removed the duplicate `Tour.price` and the vehicle seat counters (`remainingSeats`, `calculatedAvailable`); `SchemaMaintenance` drops the old `tours.price` and `transportations.remaining_seats` columns on start-up.

## 2026-11-04 (late) - Mobile parity with the web customer app

- New mobile screens: boarding pass, transaction and payment details, payments list, support requests (list, create, reply, delete), profile edit (photo, phone with country code), password reset with code, catalog filters, My reports, and Export buttons on tours, bookings, and wallet; notifications open the related screen. See [mobile](mobile/README.md).
- Shared mobile components: `SelectSheet` (searchable picker, now also behind `PhoneField`), `InfoRow`, `LinkRow`, `Avatar`, `ExportButton`; generated DTOs extended to payments, support, reports, and media.

## 2026-11-04 (night) - Server-generated reports and media

- **Server.** `ReportType` and `ReportFormat` enums, a `Media` model (`media` table) with `MediaCategory`, `MediaRepository`, `MediaService` (private storage through `FileStorageService`), `ReportDataService` (rows through the scoped domain services), `ReportService`, OpenPDF and Apache POI renderers with the same branded template as the web client, `POST /api/reports`, `GET /api/media`, `GET /api/media/{id}/download`, `DELETE /api/media/{id}`. New setting `app.media-dir` (`MEDIA_DIR`, default `./media`).
- **Web client.** Export buttons on tours, catalog, tickets, passenger manifest, fleet, meals, ledger, users, and agency branches/employees request the server report (`reportService`, `mediaService`, `useServerReport`); selected rows and guests still export in the browser.
- **Fixed during testing.** PDF footer said "of 4" on a 3-page report (OpenPDF's page counter on close); money now always shows two decimals.

## 2026-11-04 (evening) - Report template for every PDF and Excel export

- One branded template for all exports: letterhead, report meta, repeated table header, page numbers, confidentiality footer, rows kept whole, QR codes as images (PDF); typed, filterable, print-ready sheets (Excel). Import templates keep a clean header row plus an Instructions sheet. See [client](client/README.md#exports-pdf-and-excel).
- Fixed: QR/barcode images were never drawn (column keys were compared with column indexes), long cells crushed other columns, and rows split across pages. Removed the unused `excelMapper.ts` and the `xlsx` dependency.

## 2026-11-04 (later) - DTOs everywhere, sign-in, profile, and a full review

- **Server DTOs.** Every request and response is a Java record, one type per file. Responses build themselves with `from(entity)`; `ModelMapper` and the three mapper classes were removed. 28 nested summary classes became 11 shared summary records (`UserSummary`, `CountrySummary`, `TourSummary`, `SeatSummary`, ...). `PageResponse` and `EntityReference` are records. Filter DTOs stay classes (inherited paging fields, query binding). Wire names are unchanged.
- **Client DTOs.** The web client and the mobile app get a `src/dtos/<domain>/` layer generated from the server records (`tools/generate-ts-dtos.py`). Services use the DTOs, and the hand-written read models (`Tour`, `Ticket`, `User`, ...) are now aliases of them; 26 unused hand-written request interfaces were deleted.
- **Sign-in.** Email, username, or mobile number, with the password always required. Phone numbers match in any common format.
- **Country code required.** Mobile numbers are stored as `+<country code><number>`. Register, add employee, profile, and agency contact fields use the country-code picker (Bahrain by default) on web and mobile.
- **Profile.** `GET`/`PUT /api/users/me/profile` (`ProfileResponse`: identity, agency, branch, wallet, member since). The web profile page and the mobile profile tab use it.
- **Review fixes (server).** User lists, fleet, and meals are agency-scoped; managers manage only their own branch; admin role changes keep staff in an agency; per-tour seat status filtering runs in the query; meals can be edited (`PUT /api/meals/{id}`); profile photos get new file names and old files are deleted; bookings are wallet-only; failed top-ups stay recorded; missing tour, vehicle, and meal return 404. See [security](security/README.md) items 18-24.
- **Review fixes (web).** Boarding pass and journey tracker show the real route and vehicle; agency Branches tab loads branches; the profile form edits the name and no longer offers password and image-URL fields the server ignored; meals can be edited and switched on/off; the card form no longer logs the Stripe token. See [client](client/README.md).

## 2026-11-03 - Clean-up, security, inventory, and mobile

- **Server structure.** Lower-case layer packages with domain subfolders (`controllers/tourmanagement`, `services/payment`, ...); `BaseEntity` for every model (unique `code`, audit fields, identity equality); `constants/`, `middlewares/`, `seeds/`, typed `config/properties`.
- **Removed dead code.** `PaymentProcessingService`, `BarcodeService`, the unused `AuthService`, `PricingCalculator` (old), `ExcelImportUtils`, a fake `SpringBootTest` annotation, unused ticket update/approve/confirm paths, `restoreInventory`, duplicate reminder job, `extractDialCode`, about 35 unused repository queries and 110 unused imports.
- **Merged duplicate logic.** Ticket numbering, QR codes, and pricing (`TicketIssuingService`); refund policy and ticket pricing (`PricingCalculator`); booking end-of-life steps (`BookingLifecycleService`); spreadsheet reading (`ExcelImportService`).
- **Security.** See [security review](security/README.md): configurable JWT key, DTOs instead of entities for user, agency, branch, reservation, ticket, and staff requests, ownership and agency scoping, password-reset hardening, upload validation, CORS, generic 500s.
- **Inventory.** Seats are taken per tour by active tickets (a vehicle can serve several tours), maintenance is the only stored seat state, the one-to-one ticket-seat mapping and its unique key are removed, meal rules enforced.
- **Clients.** Web client contract updates and defect fixes ([client](client/README.md)); new Expo mobile app ([mobile](mobile/README.md)).
- **Docs.** Layer-mirrored, generated reference; duplicated client use-case files and stale feature folders removed.

## 2026-11-03 (later) - Remaining contracts, WebSocket security, client structure

- Server: request DTOs for the last six entity-bound endpoints; `CountryControllers` renamed `CountryController`; WebSocket CONNECT/SUBSCRIBE authorization; `updatedAt` on edited comments; editing a running tour no longer rejects its past start date.
- Web client: services grouped by domain with export-matching names; `config/endpoints.ts`; kebab-case folders; every component, page, and hook at most 150 lines; eleven UI/contract defects fixed (see [client](client/README.md)).
- Mobile: lint clean.

## 2026-11-04 - Browser test fixes

- Server: tour responses carry country `officialName`/`flagPngUrl` and `destinationCountries`; ticket responses carry the tour's `startDate`/`endDate` (My Bookings showed "TBD").
- Web client: seats requested in cabin order (`id` ascending, not `S1, S10, S2`); tour console revenue and booking count use live tickets only and real prices; vehicle number shown instead of "TR-UNASSIGNED"; customer reservation copy removed from the admin tour header; "City, Country" no longer renders a lone comma when either is missing.
- Known design limit: the web admin console is ADMIN-only. Owners, managers, and employees use the customer pages on the web, although the server already scopes their staff endpoints by agency.

## Earlier updates

This document records the cross-cutting improvements reflected in the current server and client applications.

## API consistency

Collection endpoints use the shared `PageResponse<T>` contract:

```json
{
  "content": [],
  "page": 0,
  "size": 20,
  "totalElements": 0,
  "totalPages": 0
}
```

`PaginationUtils` normalizes page size, validates sort fields, supports `asc` and `desc`, and caps requests at 100 records. Filter DTOs expose domain-specific search, status, date-range, agency, and branch parameters. API failures use a stable envelope containing `success`, `code`, `message`, `data`, `fieldErrors`, `timestamp`, and `path`.

## Agency-backed selectors

Agency and branch selectors do not download an unlimited list to the browser. The reusable client selector requests paginated results from the server, searches after a 300 ms debounce, loads the first page for an empty query, supports additional pages, and permits deselection. Changing an agency clears an incompatible branch selection.

## Transportation and seats

- Transportation creation accepts explicit `agencyId`, optional `branchId`, and a nested `seatConfig`.
- Agency/branch ownership is validated on the server.
- The selected seat counts generate that number of physical `Seat` records; remaining capacity becomes `STANDARD` seating.
- Existing layouts support one-operation bulk reclassification when no protected seats or tours make the layout unsafe to change.
- List responses omit the lazy seat collection; detail responses fetch seats, agency, and branch explicitly. This prevents `LazyInitializationException` and N+1 list queries.
- Excel import is processed by the backend, not the browser, and reports successful and failed rows independently.

## Client architecture

- `PaginatedSearchSelect` composes Chakra UI combobox primitives around the shared `PageResponse<SelectOption>` contract.
- `DynamicForm` supports nested object paths and memoized fields, preventing expensive whole-form rerenders while typing.
- `GuidedStepsDialog` supplies reusable customer instructions on tour and ticket pages.
- The date picker supports range selection, light/dark modes, deterministic server rendering, accessible controls, and valid HTML nesting.
- Hydration-sensitive clock/browser behavior is deferred through `useIsHydrated`; notification listeners are registered and cleaned up through React effects.
- Network failures are converted to user-facing messages and handled by state-loading hooks without unhandled promise rejections.

## Configuration and repository hygiene

Runtime secrets belong in the ignored `application.properties` file or environment variables. `application.properties.example` documents required keys without real credentials. Maven repositories, logs, runtime uploads, and API-tool environment exports are excluded from source control.

