# Phase 02: Foundation

**Status:** Done
**Depends on:** Phase 01

## Goal

Shared building blocks every layer uses.

## Scope

| Layer | Folders | Items |
| --- | --- | --- |
| Server | `config/`, `constants/`, `enums/`, `models/base/`, `utilities/`, `middlewares/` | Typed `AppProperties`, `ErrorCodes`, `BaseEntity`, `ApiResponse`, `CodeGenerator`, pagination, JWT, error handling, rate limit, request ids |
| Clients | `config/`, `services/` | One API client per app, endpoint maps under `/api/v1` |

## Tasks

- [x] Validated configuration that fails startup on bad values
- [x] One response envelope with an error code for every failure
- [x] Base entity with `id`, unique `code` and audit fields
- [x] Generic pagination request and response
- [x] Middlewares for authentication, errors, logging with request ids, and auth rate limiting

## Acceptance criteria

- Server starts with validated config
- Utilities have unit tests

## Verification

| Check | Command or steps | Result |
| --- | --- | --- |
| Unit tests | `./mvnw verify` | 79 passed (2026-11-05) |

## Risks and open questions

- None.
