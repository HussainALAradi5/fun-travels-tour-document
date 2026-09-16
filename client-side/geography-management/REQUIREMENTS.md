# Geography Management Requirements

## Requirement catalog

| ID | Type | Priority | Requirement | Verification |
|---|---|---|---|---|
| RQ-1 | Functional | Medium | The module shall support GET /api/countries to populate country selection. | Endpoint integration test |
| RQ-2 | Functional | High | The module shall support POST /api/countries to add a country manually. | Endpoint integration test |
| RQ-3 | Functional | High | The module shall support POST /api/countries/sync/{name} to import one country from the external provider. | Endpoint integration test |
| RQ-4 | Functional | High | The module shall support POST /api/countries/sync-all to synchronize the country catalog. | Endpoint integration test |
| RQ-5 | Functional | High | The module shall support DELETE /api/countries/{id} to remove a country. | Endpoint integration test |
| RQ-6 | Functional | Medium | The module shall support GET /api/cities to populate city selection. | Endpoint integration test |
| RQ-7 | Functional | Medium | The module shall support GET /api/cities/country/{countryId} to return cities within a country. | Endpoint integration test |
| RQ-8 | Functional | High | The module shall support POST /api/cities to add a city. | Endpoint integration test |
| RQ-9 | Functional | High | The module shall support DELETE /api/cities/{id} to remove a city. | Endpoint integration test |
| RQ-10 | Functional | Medium | The module shall support GET /api/ports to list active transport ports. | Endpoint integration test |
| RQ-11 | Functional | High | The module shall support POST /api/ports to create a transport port. | Endpoint integration test |
| RQ-12 | Functional | High | The module shall support PUT /api/ports/{id}/status to change port lifecycle status. | Endpoint integration test |
| RQ-13 | Non-functional | Very High | The server shall enforce authentication, authorization, and ownership independently of client visibility. | Security integration test |
| RQ-14 | Non-functional | Very High | Multi-record state changes shall be transactional and rollback on failure. | Transactional integration test |
| RQ-15 | Non-functional | High | Failures shall use stable codes and user-readable messages without exposing stack traces. | Error-contract test |
| RQ-16 | Non-functional | Medium | Collection operations shall use bounded pagination, safe sorting, and explicit loading or empty states. | Pagination/UI test |
| RQ-17 | Non-functional | Medium | Important state transitions shall be observable through audit data or structured logs. | Audit/log verification |

## Priority definition

- Very High: security, money, booking integrity, inventory, or irreversible state.
- High: core business capability or mutation.
- Medium: read-only discovery, usability, observability, or operational convenience.

## Traceability

Each RQ maps to an endpoint/service function, one or more UC entries, and the related WF/FC processes.

