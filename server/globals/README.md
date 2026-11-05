# Server globals

| Topic | Page |
| --- | --- |
| Configuration and environment | [configuration.md](configuration.md) |
| Authentication, rate limiting, request ids, roles, ownership | [security.md](security.md) |
| Error envelope and codes | [errors.md](errors.md) |
| Pagination and sorting | [pagination.md](pagination.md) |
| Flyway migrations and development seed | [schema-and-seeds.md](schema-and-seeds.md) |

## Code layout

```text
src/main/java/com/server/server/
  config/        database (auditing), notification, payment, properties, scheduling, security, web
  constants/     common, errors (ErrorCodes), report, tourmanagement, user (RoleGroups)
  controllers/   agency, auth, geography, media, notification, payment, report, support, tourmanagement, user
  dto/           common and the same domain folders
  enums/         common and the same domain folders
  exceptions/    common: named exceptions services throw
  middlewares/   auth (JWT filter, WebSocket auth), errors (GlobalExceptionHandler, SecurityErrorResponder),
                 logging (RequestIdFilter), security (AuthRateLimitFilter)
  models/        base (BaseEntity) + domain folders
  repositories/  domain folders
  seeds/         development: DataSeeder
  services/      auth, common, domain folders
  utilities/     codes, filters, pagination, phone, pricing, report, responses
  validations/   workflow: DomainWorkflowValidator
src/main/resources/db/migration/   Flyway scripts
```
