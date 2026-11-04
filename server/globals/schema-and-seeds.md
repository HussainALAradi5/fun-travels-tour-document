# Schema maintenance and seeds

## Schema

Hibernate `ddl-auto=update` creates and extends tables. Because it never drops constraints, `config/database/SchemaMaintenance` runs ordered, idempotent fixes on every start:

1. Drops the legacy unique key on `tickets.seat_id`. Tickets used to map their seat one-to-one, which let a seat appear on only one ticket ever (even after cancellation or on a later tour). Verified against a database that had the constraint.

All models now share `BaseEntity` columns (`code` unique, `created_at`, `updated_at`, `created_by_id`, `updated_by_id`); existing rows keep a null `code` until they are re-saved. Adopting Flyway for versioned migrations is recommended before production.

## Development seed

`seeds/DataSeeder` runs only when `app.seed.enabled=true`, never under the `prod` profile, and only when the user table is empty. It creates one agency, one branch, and one user per role. The shared password comes from `SEED_PASSWORD`; when empty, a random one is written to `seed-credentials.local.txt` (git-ignored).
