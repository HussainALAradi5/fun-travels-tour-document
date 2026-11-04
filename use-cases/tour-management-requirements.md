# Tour Management Requirements

## Requirement catalog

| ID | Type | Priority | Requirement | Verification |
|---|---|---|---|---|
| RQ-1 | Functional | Medium | The module shall support GET /api/tours/catalog to browse currently bookable tours. | Endpoint integration test |
| RQ-2 | Functional | Medium | The module shall support GET /api/tours/search to search operational tours. | Endpoint integration test |
| RQ-3 | Functional | Medium | The module shall support GET /api/tours to list tours with bounded pagination. | Endpoint integration test |
| RQ-4 | Functional | Medium | The module shall support GET /api/tours/{id} to view one tour. | Endpoint integration test |
| RQ-5 | Functional | High | The module shall support POST /api/tours to create and validate a tour. | Endpoint integration test |
| RQ-6 | Functional | High | The module shall support PUT /api/tours/{id} to update editable tour details. | Endpoint integration test |
| RQ-7 | Functional | High | The module shall support PUT /api/tours/{id}/status to execute a tour workflow transition. | Endpoint integration test |
| RQ-8 | Functional | High | The module shall support POST /api/transportations to register a unit and generate its seats. | Endpoint integration test |
| RQ-9 | Functional | High | The module shall support POST /api/transportations/imports to import multiple transport units server-side. | Endpoint integration test |
| RQ-10 | Functional | Medium | The module shall support GET /api/transportations to list transport units. | Endpoint integration test |
| RQ-11 | Functional | Medium | The module shall support GET /api/transportations/{id} to view a unit with seat details. | Endpoint integration test |
| RQ-12 | Functional | High | The module shall support PUT /api/transportations/{id} to update scalar fields or safe seat layout. | Endpoint integration test |
| RQ-13 | Functional | High | The module shall support PATCH /api/transportations/{id}/status to change operational unit status. | Endpoint integration test |
| RQ-14 | Functional | Medium | The module shall support GET /api/transportations/search to search the fleet using server filters. | Endpoint integration test |
| RQ-15 | Functional | Medium | The module shall support GET /api/seats to list seats with pagination. | Endpoint integration test |
| RQ-16 | Functional | Medium | The module shall support GET /api/seats/{id} to view one seat. | Endpoint integration test |
| RQ-17 | Functional | High | The module shall support PATCH /api/seats/{id} to configure an editable seat. | Endpoint integration test |
| RQ-18 | Functional | Medium | The module shall support GET /api/seats/search to filter seats by unit, class, status, or code. | Endpoint integration test |
| RQ-19 | Functional | High | The module shall support PATCH /api/seats/{id}/status to change operational seat status. | Endpoint integration test |
| RQ-20 | Functional | Medium | The module shall support GET /api/meals to list meal plans. | Endpoint integration test |
| RQ-21 | Functional | Medium | The module shall support GET /api/meals/agency/{agencyId} to show an agency meal catalog. | Endpoint integration test |
| RQ-22 | Functional | High | The module shall support POST /api/meals to define a meal offering. | Endpoint integration test |
| RQ-23 | Functional | High | The module shall support PATCH /api/meals/{id}/status to enable or disable a meal. | Endpoint integration test |
| RQ-24 | Functional | High | The module shall support PUT /api/meals/{id}/price to update meal pricing. | Endpoint integration test |
| RQ-25 | Functional | Very High | The module shall support POST /api/reservations to create a 15-minute booking hold. | Endpoint integration test |
| RQ-26 | Functional | Very High | The module shall support PATCH /api/reservations/{id}/status to perform an authorized reservation transition. | Endpoint integration test |
| RQ-27 | Functional | Very High | The module shall support PATCH /api/reservations/{id}/cancel to cancel, refund when eligible, and release inventory. | Endpoint integration test |
| RQ-28 | Functional | Very High | The module shall support GET /api/reservations/search to search reservations with role scoping. | Endpoint integration test |
| RQ-29 | Functional | Very High | The module shall support GET /api/reservations to list role-scoped reservations. | Endpoint integration test |
| RQ-30 | Functional | Very High | The module shall support GET /api/reservations/{id} to view one authorized reservation. | Endpoint integration test |
| RQ-31 | Functional | Very High | The module shall support GET /api/tickets/search to search role-scoped tickets. | Endpoint integration test |
| RQ-32 | Functional | Very High | The module shall support GET /api/tickets to list role-scoped tickets. | Endpoint integration test |
| RQ-33 | Functional | Very High | The module shall support GET /api/tickets/{id} to view one authorized ticket. | Endpoint integration test |
| RQ-34 | Functional | Very High | The module shall support POST /api/tickets to create a ticket and generate codes. | Endpoint integration test |
| RQ-35 | Functional | Very High | The module shall support PUT /api/tickets/{id}/status to execute a ticket approval transition. | Endpoint integration test |
| RQ-36 | Functional | Very High | The module shall support PUT /api/tickets/{id}/cancel to cancel a ticket and release its inventory. | Endpoint integration test |
| RQ-37 | Functional | Very High | The module shall support PUT /api/tickets/{id}/approve to approve a paid ticket. | Endpoint integration test |
| RQ-38 | Functional | Very High | The module shall support PUT /api/tickets/{id}/confirm to confirm an approved ticket. | Endpoint integration test |
| RQ-39 | Non-functional | Very High | The server shall enforce authentication, authorization, and ownership independently of client visibility. | Security integration test |
| RQ-40 | Non-functional | Very High | Multi-record state changes shall be transactional and rollback on failure. | Transactional integration test |
| RQ-41 | Non-functional | High | Failures shall use stable codes and user-readable messages without exposing stack traces. | Error-contract test |
| RQ-42 | Non-functional | Medium | Collection operations shall use bounded pagination, safe sorting, and explicit loading or empty states. | Pagination/UI test |
| RQ-43 | Non-functional | Medium | Important state transitions shall be observable through audit data or structured logs. | Audit/log verification |

## Priority definition

- Very High: security, money, booking integrity, inventory, or irreversible state.
- High: core business capability or mutation.
- Medium: read-only discovery, usability, observability, or operational convenience.

## Traceability

Each RQ maps to an endpoint/service function, one or more UC entries, and the related WF/FC processes.

