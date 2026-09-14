# Server Documentation

The backend is a Java 21 and Spring Boot 3.5.16 REST application backed by PostgreSQL.

## Architecture

| Layer | Responsibility |
|---|---|
| Controllers | HTTP routing, validation, authorization, and response envelopes |
| Services | Transactions, workflows, conflict checks, and orchestration |
| Repositories | Spring Data JPA queries, specifications, locks, and entity graphs |
| DTOs and mappers | Stable API contracts without exposing persistence graphs |
| Utilities | Pagination, filtering, workflow validation, Excel parsing, and mapping |
| Exceptions | Consistent user-safe errors through `GlobalExceptionHandler` |

## Local setup

1. Install Java 21 and PostgreSQL.
2. Create the `fun_travels_tour` database.
3. Copy `src/main/resources/application.properties.example` to `application.properties`.
4. Configure database, JWT, payment, and optional mail credentials.
5. Run `./mvnw spring-boot:run` (`.\mvnw.cmd spring-boot:run` on Windows).

The API starts at `http://localhost:8080/api` by default.

## Shared collection contract

Paginated endpoints accept `page`, `size`, `sortBy`, and `sortDir`. Search endpoints add domain filters such as `search`, `startDate`, `endDate`, `status`, `agencyId`, and `branchId`. Unsupported sort fields and directions are rejected with clear client-safe messages.

## Security and integrity

- Stateless JWT authentication and BCrypt password hashing
- Method-level role authorization
- Transactional workflow operations
- Pessimistic locking for contention-sensitive inventory
- DTO responses that avoid recursive or lazy entity serialization
- Central validation and exception translation

See the domain folders for endpoint and service contracts.
See the [complete endpoint reference](ENDPOINT_REFERENCE.md) for the URL-to-service/function mapping and the [platform services](platform-services/) section for shared infrastructure.
