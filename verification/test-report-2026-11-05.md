# Test report: Fun Travels Tour (2026-11-05)

**Scope:** Server, web client, mobile, documentation
**Skills:** `reusable-fullstack-skills` (project-testing, clean-code-standards, server/client/mobile workflows, fullstack-contracts, documentation-workflow)
**Branch and commit:** server `main` @ `cf6549c`, client `main` @ `016068b`, mobile `master` @ `02449db`, document `main` @ `0dc30de`
**Requirements sources:** `use-cases/tour-management-requirements.md` (RQ-1 to RQ-43), use cases, user requests. There is no `phases/` folder.

## Fixes (2026-11-05, evening)

Every finding below was fixed on its own branch except where the Outcome says otherwise. Results are in [verification](README.md).

| Finding | Outcome | Branch |
| --- | --- | --- |
| Unknown routes and wrong methods returned 500 | Fixed: 404 `ROUTE_NOT_FOUND`, 405 `METHOD_NOT_ALLOWED` | server `fix/error-codes-and-exceptions` |
| Errors all used `REQUEST_FAILED` | Fixed: `ErrorCodes` constants on every handler; security 401 and 403 use the envelope | server `fix/error-codes-and-exceptions` |
| `IllegalStateException` for disk and external failures (409, leaked setting name) | Fixed: `StorageException` (500), `ExternalServiceException` (502), generic messages | server `fix/error-codes-and-exceptions` |
| Port and notification recipient not found gave 400 and 500 | Fixed: `ResourceNotFoundException` (404) | server `fix/error-codes-and-exceptions` |
| Nightly task failures logged without stack trace | Fixed; and found that nightly jobs ran without transactions (now one transaction each) | server `fix/error-codes-and-exceptions`, `fix/eager-loading` |
| No ordered migrations | Fixed: Flyway V1 baseline, V2 retired columns and indexes; Hibernate validates | server `add/flyway-migrations` |
| No indexes | Fixed: 53 indexes in V2 | server `add/flyway-migrations` |
| 17 eager relations, N+1 per row | Fixed: lazy relations, batch fetching, inverse account mapping removed; 124 to 52 statements over ten lists | server `fix/eager-loading` |
| No auth rate limit | Fixed: `AuthRateLimitFilter` | server `add/request-middlewares` |
| No request ids in logs | Fixed: `RequestIdFilter` | server `add/request-middlewares` |
| No versioned API prefix | Fixed: `/api/v1` from `app.api-prefix`, web and mobile updated | server, client, mobile `refactor/api-version-prefix` |
| Flat server layers, no `validations/` | Fixed: domain subfolders, `validations/workflow` | server `refactor/layer-subfolders` |
| Local types in web and mobile render files | Fixed (the Chakra CLI snippets in `components/ui` stay as generated) | client `refactor/types-and-image-constants`, mobile `refactor/local-types` |
| Hardcoded banner image URLs | Fixed: `constants/ui/images.ts` | client `refactor/types-and-image-constants` |
| No `phases/` folder | Fixed: nine phase files and an index | document `docs/review-fixes` |
| Service docs without cases and exceptions; controller tables without exceptions | Fixed: generated from the code | document `docs/review-fixes` |
| `findAll()` on agencies, branches, cities and countries | Kept: small reference and admin lists; batch fetching removes their per-row queries | - |
| AI attribution trailers in 30 past commits | Not changed: removing them rewrites published history and needs force pushes; new commits carry none | - |
| Mobile not run on a device | Still open (phase 07) | - |

## Builds and existing tests

| Part | Command | Result |
| --- | --- | --- |
| Server build and unit tests | `./mvnw -B verify` (clean clone) | Passed, 69 tests |
| Server CI | GitHub Actions run 42044859992 | Passed (first run failed, see S-1) |
| Live API suites | 7 scripts against a fresh database | 217/217 passed |
| Web | GitHub Actions run 42043432838 (`typecheck`, `lint`, `build`) | Passed |
| Mobile | `npm ci`, `typecheck`, `lint`, `expo export --platform android` (clean clone) | Passed |
| Mobile CI | GitHub Actions | Not checked (private repository) |
| Mobile on a device or emulator | - | Not run |

## Server

### 1. Logic
No new findings. Booking, holds, inventory recount, seats, meals, refunds, wallet, reports and visibility pass the live suites (217 checks).

### 3. Errors
| Severity | Location | Finding | Fix |
| --- | --- | --- | --- |
| Medium | `exceptions/GlobalExceptionHandler.java:133` | Unknown routes (`NoResourceFoundException`) and wrong methods (`HttpRequestMethodNotSupportedException`) fall into the catch-all: 500 plus an ERROR stack trace, instead of 404 and 405 | Add handlers for both |
| Medium | `exceptions/GlobalExceptionHandler.java:139` | Most errors carry the code `REQUEST_FAILED`; only workflow errors have specific codes | Error-code constants (`NOT_FOUND`, `CONFLICT`, `FORBIDDEN`, `VALIDATION_FAILED`, ...) set by each handler |
| Medium | `exceptions/GlobalExceptionHandler.java:128` | `IllegalStateException` maps to 409, but file I/O failures use it (`FileStorageService.java:49,80,88`) and so does the missing-API-key error (`CountryService.java:155`), which also shows the setting name to the caller | Storage failure and external-service exceptions (500 or 502 with a generic message) |
| Low | `services/common/SystemSchedulingService.java:34` | A failed nightly task logs only its message, not the stack trace | Log the exception |

### 4. Inconsistent logic or code
| Severity | Location | Finding | Fix |
| --- | --- | --- | --- |
| Low | Server routes vs. skill | Routes are `/api/...`; the standard asks for a versioned prefix (`/api/v1`) kept in config | Optional; touches every client endpoint map |

### 5. Clean code
| Severity | Location | Finding | Fix |
| --- | --- | --- | --- |
| Medium | `config/database/SchemaMaintenance.java`, `ddl-auto=update` | No ordered migrations | Flyway baseline plus versioned scripts |
| Medium | `middlewares/` | No rate limiting on sign-in, registration or password reset | Rate-limit middleware for `/api/auth/**` |
| Low | `middlewares/` | No request ID or request logging middleware | Request-ID filter (MDC) |
| Low | `constants/`, `exceptions/`, `utilities/`, `middlewares/` | Flat folders; the standard wants domain subfolders in every layer | Move files into domain subfolders |
| Low | - | No `validations/` layer; checks live in DTO annotations and `DomainWorkflowValidator` | Acceptable for Spring (constraint annotations); move the validator to `validations/` |
| OK | `models/base/BaseEntity.java` | Every model extends the base entity: `id`, unique `code`, audit fields set automatically | - |
| OK | `seeds/` | One user per role, development only, refused under `prod` | - |

### 6. Requirements met
All 43 requirements map to implemented endpoints (checked against the generated controller tables). RQ-39 (server-side access) and RQ-40 (transactions) are covered by the access and booking suites.

### 7. Optimization
| Item | Location | Measured | Change |
| --- | --- | --- | --- |
| Eager relations | 17 `FetchType.EAGER`, including `Agency.branches` (one-to-many) in `models/agency/Agency.java:70` | `GET /api/agencies`: 8 queries on seed data; grows with agencies and branches | Make them lazy; fetch what each DTO needs with entity graphs |
| Page queries | `GET /api/tours` 18 queries, `GET /api/tickets` 17 queries for one page of seed data | N+1 per row | Entity graphs or join fetch on list queries |
| Missing indexes | No `@Index` on any model; PostgreSQL does not index foreign keys | Not measured (small data) | Index foreign keys and filter fields (status, dates, recipient, customer, tour) |
| Unbounded lists | `findAll()` in `AgencyService:47`, `AgencyBranchService:39`, `CityService:31`, `CountryService:51` | Admin and reference lists | Acceptable for reference data; page the agency and branch lists |

### 9. Roles and permissions
Each seeded role was exercised in the access suite (32 checks): agency scoping, branch scoping, customer ownership, report roles, media ownership. No failures.

### 10. Exceptions exist
| Service function | Failure case | Expected | Actual |
| --- | --- | --- | --- |
| `PortService` (line 43) | Port not found | `ResourceNotFoundException` (404) | `IllegalArgumentException`, so 400 |
| `NotificationService` (line 97) | Recipient not found | `ResourceNotFoundException` (404) | `RuntimeException`, so 500 |
| `FileStorageService` | Disk write or read fails | Storage failure (500) | `IllegalStateException`, so 409 |
| `CountryService.fetch*` | External API not configured or failing | External-service failure (502) | `IllegalStateException`, so 409 |

## Web client

| Check | Severity | Location | Finding | Fix |
| --- | --- | --- | --- | --- |
| Clean code | Low | `app/client-shell.tsx`, `components/auth/RouteGuard.tsx`, `components/Footer.tsx`, `components/ui/custom/DataTable.tsx`, `hooks/tour-management/useCatalogFilters.tsx`, `lib/navigation.tsx` | Props and helper types declared in render or hook files | Move to `interfaces/` or `types/` |
| Clean code | Low | 16 page files (for example `components/pages/HomePage.tsx:56`) | Hardcoded banner image URLs | One constants file |
| Clean code | OK | - | No file over 150 lines; no network calls in components; one API client | - |

## Mobile

| Check | Severity | Location | Finding | Fix |
| --- | --- | --- | --- | --- |
| Clean code | Low | `components/tour/CatalogFilters.tsx:12` | Local type | Move to `types/` |
| Logic and roles | - | - | Not run on a device or emulator | Run the core flows on Android |
| Clean code | OK | - | No file over 150 lines; screens get state from hooks; one fetch client; tokens in secure storage | - |

## Documentation

| Check | Severity | Location | Finding | Fix |
| --- | --- | --- | --- | --- |
| Phases | High | - | No `phases/` folder with phase files and an index | Add the nine phases with status and verification |
| Documentation | Medium | `server/services/**` | Functions list signature, purpose and transaction, but not cases covered or exceptions | Generate exceptions per function from the code |
| Documentation | Medium | `server/controllers/**` | Endpoint tables have no Exceptions column | Add it from the same source |
| Clean code | Medium | git history | 30 commits carry an AI `Co-Authored-By` trailer; rule 40 forbids them | Stop adding them; rewriting history needs force pushes and is your call |

## Summary

| Check | Server | Web | Mobile | Docs |
| --- | --- | --- | --- | --- |
| Logic | OK | OK | Not tested on device | - |
| Documentation | - | - | - | 2 medium |
| Errors | 3 medium, 1 low | OK | OK | - |
| Inconsistent | 1 low | OK | OK | - |
| Clean code | 2 medium, 3 low | 2 low | 1 low | 1 medium |
| Requirements | OK (43/43) | OK | OK | - |
| Optimization | 2 medium, 1 medium (indexes) | OK | OK | - |
| Phases | - | - | - | 1 high |
| Roles and permissions | OK | OK | Not tested on device | - |
| Exceptions exist | 4 findings (medium) | - | - | - |

**Overall:** Working and secure, with no critical findings. Under the new standard, the remaining work is the error and exception mapping, query loading and indexes, rate limiting, the phases folder, and the exception columns in the docs.
