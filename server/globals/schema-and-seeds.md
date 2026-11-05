# Schema migrations and seeds

## Schema

Flyway owns the schema. Versioned scripts live in the server's `src/main/resources/db/migration` and run on startup, before the application uses the database. Hibernate only validates that the tables match the entities (`spring.jpa.hibernate.ddl-auto=validate`), so a missing column fails the start instead of being created silently.

| Version | Script | What it does |
| --- | --- | --- |
| 1 | `V1__baseline.sql` | The full schema generated from the entities: 23 tables, identity keys, unique codes, foreign keys, enum check constraints |
| 2 | `V2__retired_columns_and_indexes.sql` | Drops `tours.price`, `transportations.remaining_seats` and the old unique key on `tickets.seat_id` (a seat can be booked again after a cancellation); adds 53 indexes on foreign keys and on the columns lists filter by (tour status and start date, reservation status and hold expiry, notification recipient and read flag, report category and date, request and payment status, unit status, user type) |

Audit foreign keys (`created_by_id`, `updated_by_id`) are not indexed: nothing filters on them.

**Existing databases.** A database created before migrations existed (by Hibernate `update`) is marked as version 1 (`spring.flyway.baseline-on-migrate=true`, `baseline-version=1`) and receives only version 2. Verified on a copy built by Hibernate with the retired column and constraint added back: both were dropped and all indexes created.

**Changing the schema.** Add `V<n>__<description>.sql`; never edit a script that has already run, because Flyway checks each applied script's checksum.

All models share `BaseEntity` columns (`code` unique, `created_at`, `updated_at`, `created_by_id`, `updated_by_id`).

## Development seed

`seeds/development/DataSeeder` runs only when `app.seed.enabled=true`, never under the `prod` profile, and only when the user table is empty. It creates one agency, one branch, and one user per role. The shared password comes from `SEED_PASSWORD`; when empty, a random one is written to `seed-credentials.local.txt` (git-ignored).
