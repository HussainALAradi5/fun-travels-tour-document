# Phase 05: Client foundation

**Status:** Done
**Depends on:** Phase 04

## Goal

Web client wired to the API.

## Scope

| Layer | Folders | Items |
| --- | --- | --- |
| Web | `config/`, `services/`, `dtos/`, `interfaces/`, `enums/`, `utilities/` | Generated DTO mirrors, one axios client, route guards |

## Tasks

- [x] Endpoint map matching server routes
- [x] Generated TypeScript DTOs
- [x] Auth context and route guards

## Acceptance criteria

- Client builds and signs in against the running server

## Verification

| Check | Command or steps | Result |
| --- | --- | --- |
| Web checks | `npm run typecheck`, `npm run lint`, `npm run build` | Passed (2026-11-05) |

## Risks and open questions

- None.
