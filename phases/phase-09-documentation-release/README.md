# Phase 09: Documentation and release

**Status:** In progress
**Depends on:** Phase 08

## Goal

Complete documentation and ship.

## Scope

| Layer | Folders | Items |
| --- | --- | --- |
| Docs | `server/`, `client/`, `mobile/`, `use-cases/`, `setup/`, `security/`, `verification/` | Generated reference, use cases, setup, security review |

## Tasks

- [x] Generated service and controller reference with cases and exceptions
- [x] Setup guide and settings
- [ ] Pull requests for the review fixes
- [ ] Deployment

## Acceptance criteria

- Docs match the code
- Release checks pass
- The application runs in a shared environment

## Verification

| Check | Command or steps | Result |
| --- | --- | --- |
| Reference | `tools/generate-reference.py` | Regenerated 2026-11-05 |
| Deployment | - | Not done |

## Risks and open questions

- No hosting target is chosen yet; see the server README for the settings a deployment needs.
