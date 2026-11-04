# Server globals

| Topic | Page |
| --- | --- |
| Configuration and environment | [configuration.md](configuration.md) |
| Authentication filter, roles, ownership | [security.md](security.md) |
| Error envelope and codes | [errors.md](errors.md) |
| Pagination and sorting | [pagination.md](pagination.md) |
| Schema maintenance and development seed | [schema-and-seeds.md](schema-and-seeds.md) |

## Code layout

```text
src/main/java/com/server/server/
  config/        database, notification, payment, properties, scheduling, security, web
  constants/     BookingRules, CodePrefixes, RoleGroups, ValidationPatterns
  controllers/   agency, auth, geography, notification, payment, support, tourmanagement, user
  dto/           common, agency, auth, geography, notification, payment, support, tourmanagement, user
  enums/         common, geography, notification, payment, support, tourmanagement, user
  exceptions/    domain exceptions and GlobalExceptionHandler
  middlewares/   JwtAuthenticationFilter
  models/        base (BaseEntity) + domain folders
  repositories/  domain folders
  seeds/         DataSeeder (development only)
  services/      auth, common, domain folders
  utilities/     ApiResponse, CodeGenerator, DomainWorkflowValidator, FilterUtils, PaginationUtils, PricingCalculator, mappers
```
