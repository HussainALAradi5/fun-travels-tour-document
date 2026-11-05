# Phase 04: Server logic

**Status:** Done
**Depends on:** Phase 03

## Goal

The API: DTOs, validations, services and controllers for every use case.

## Scope

| Layer | Folders | Items |
| --- | --- | --- |
| Server | `dto/`, `validations/`, `services/`, `controllers/` | 22 controllers, record DTOs, booking, inventory, payments, reports |

## Tasks

- [x] Request and response records for every endpoint
- [x] Server-side roles, ownership and agency scoping
- [x] Transactional booking, inventory recount, refunds and wallet
- [x] Server-generated PDF and Excel reports
- [x] Named exceptions with status and code for every failure case

## Acceptance criteria

- Every endpoint returns the documented DTOs and errors
- Service rules have tests

## Verification

| Check | Command or steps | Result |
| --- | --- | --- |
| Live API suites | 7 scripts against a fresh database | 217 of 217 passed (2026-11-05) |
| Role checks | `access_check`: every seeded role, allowed and forbidden calls | 32 of 32 passed |

## Risks and open questions

- None.
