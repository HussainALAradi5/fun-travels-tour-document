# Fun Travels Tour Documentation

> Technical and business documentation for a multi-agency travel operations platform.

**Author:** Hussain Al Aradi - [GitHub](https://github.com/HussainALAradi5)

## Repositories

| Application | Stack | Repository | Setup |
| --- | --- | --- | --- |
| Server | Java 21, Spring Boot 3.5.16, Spring Data JPA, PostgreSQL | [fun-travels-tour-server](https://github.com/HussainALAradi5/fun-travels-tour-server) | [setup](setup/README.md#server) |
| Web client | Next.js 16, React 19, TypeScript, Chakra UI 3 | [fun-travels-tour-client](https://github.com/HussainALAradi5/fun-travels-tour-client) | [setup](setup/README.md#web-client) |
| Mobile app | Expo SDK 58, React Native 0.88, Expo Router, TypeScript | local repository `fun-travels-tour-mobile` (no remote yet) | [setup](setup/README.md#mobile-app) |

## Documentation map

The layout mirrors the code layers, not features.

| Section | Contents |
| --- | --- |
| [server/models](server/models/README.md) | Every model, its fields, and the relationship table |
| [server/services](server/services/README.md) | Every service function with signature; business rules for workflow services |
| [server/controllers](server/controllers/README.md) | Every endpoint: method, path, service function, role, request and response DTO |
| [server/dto](server/dto/README.md) | Every request and response record with fields and validation rules; how clients mirror them |
| [server/enums](server/enums/README.md) / [server/constants](server/constants/README.md) | Enumerations and shared rule values |
| [server/globals](server/globals/README.md) | Configuration, security filters, errors, pagination, schema maintenance, seeds |
| [client](client/README.md) | Web client layers, services, and contract notes |
| [mobile](mobile/README.md) | Mobile app layers, screens, and device notes |
| [use-cases](use-cases/README.md) | Actor, preconditions, main and failure flows, result |
| [security](security/README.md) | Access rules, review findings and fixes, known limitations |
| [setup](setup/README.md) | Running each repository locally |
| [verification](verification/README.md) | What was built, tested, and exercised, with results |
| [Personas](PERSONAS.md) / [Software engineering](SOFTWARE_ENGINEERING.md) | Personas and engineering artifacts |
| [Implementation updates](IMPLEMENTATION_UPDATES.md) | Change history |

`server/` reference pages are generated from the server source by `tools/generate-reference.py`; the business-logic sections come from `tools/service-logic/`. Regenerate after server changes:

```bash
python tools/generate-reference.py ../fun-travels-tour-server .
```

After changing a server DTO, regenerate the client mirrors too:

```bash
python tools/generate-ts-dtos.py ../fun-travels-tour-server/src/main/java/com/server/server/dto ../fun-travels-tour-client/src web
python tools/generate-ts-dtos.py ../fun-travels-tour-server/src/main/java/com/server/server/dto ../fun-travels-tour-mobile/src mobile
```

## Roles

| Role | Responsibility | Data scope |
| --- | --- | --- |
| `ADMIN` | Platform administration | Everything |
| `OWNER` | Agency, branches, staff, fleet, tours | Own agency |
| `MANAGER` | Branch operations | Own agency (tours: own branch) |
| `EMPLOYEE` | Day-to-day operations | Own agency (tours: ones they created) |
| `CUSTOMER` | Discovery, booking, payment, tickets | Own records |
| `SUPPORT_AGENT` | Support requests | Support requests |
| `DEVELOPER` | Reserved; no permissions beyond sign-in | Own profile |

Development seed accounts are listed in [setup](setup/README.md#seeded-accounts).
