# Phase 08: Quality

**Status:** Done
**Depends on:** Phase 04 (covers the web and mobile code written so far)

## Goal

Make the code safe, clean and fast.

## Scope

| Layer | Folders | Items |
| --- | --- | --- |
| All | Server, web, mobile | Security review, project-testing review, duplication, dead code, query performance |

## Tasks

- [x] Security review (34 findings fixed)
- [x] Project-testing review against the clean-code standards
- [x] Error codes and named exceptions
- [x] Lazy loading, batch fetching and indexes
- [x] Layer subfolders, local types and image constants

## Acceptance criteria

- Findings fixed or listed
- Builds and tests pass

## Verification

| Check | Command or steps | Result |
| --- | --- | --- |
| Test report | [test-report-2026-11-05](../../verification/test-report-2026-11-05.md) | All findings fixed except the ones listed there |
| Query counts | SQL statements per list request | 124 to 52 across ten list requests |

## Risks and open questions

- None.
