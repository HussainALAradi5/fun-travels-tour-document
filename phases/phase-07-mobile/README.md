# Phase 07: Mobile

**Status:** In progress
**Depends on:** Phase 04

## Goal

Expo app with full customer parity on the same API.

## Scope

| Layer | Folders | Items |
| --- | --- | --- |
| Mobile | `src/app`, `src/hooks`, `src/services`, `src/components` | Catalog, booking, wallet, tickets, notifications, support, profile, reports |

## Tasks

- [x] Screens for every customer use case
- [x] Secure token storage
- [x] Reports download and share
- [ ] Run the core flows on an Android emulator or a phone

## Acceptance criteria

- Core use cases work on an emulator or device

## Verification

| Check | Command or steps | Result |
| --- | --- | --- |
| Static checks | `npm run typecheck`, `npm run lint`, `npx expo export --platform android` | Passed (2026-11-05) |
| API contract | `mobile_contract`, `mobile_contract2` | 44 of 44 passed |
| Emulator or device | - | Not run |

## Risks and open questions

- The acceptance criterion needs a run on an Android emulator or a phone.
