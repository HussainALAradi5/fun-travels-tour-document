# Phase 03: Data

**Status:** Done
**Depends on:** Phase 02

## Goal

Persisted models, versioned migrations, indexes and development data.

## Scope

| Layer | Folders | Items |
| --- | --- | --- |
| Server | `models/`, `repositories/`, `src/main/resources/db/migration/`, `seeds/development/` | 23 tables, Flyway V1 baseline and V2 indexes, one seeded user per role |

## Tasks

- [x] Model relationships with owning sides and lazy loading
- [x] Flyway baseline generated from the entities
- [x] Index foreign keys and filter columns
- [x] Development seed refused under `prod`

## Acceptance criteria

- Migrations run on an empty database
- An existing Hibernate-created database is baselined and upgraded
- The seed creates every role

## Verification

| Check | Command or steps | Result |
| --- | --- | --- |
| Fresh database | Server start on an empty database | V1 and V2 applied, schema validated, 7 users seeded |
| Upgrade | Start on a Hibernate-built database with a retired column | Baselined at 1, V2 applied, column dropped |

## Risks and open questions

- None.
