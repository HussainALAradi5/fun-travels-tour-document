# Agency Management Requirements

## Requirement catalog

| ID | Type | Priority | Requirement | Verification |
|---|---|---|---|---|
| RQ-1 | Functional | High | The module shall support POST /api/agencies to create an agency and resolve owner/geography references. | Endpoint integration test |
| RQ-2 | Functional | Medium | The module shall support GET /api/agencies/{id} to view one agency. | Endpoint integration test |
| RQ-3 | Functional | Medium | The module shall support GET /api/agencies/search to power the paginated remote agency selector. | Endpoint integration test |
| RQ-4 | Functional | Medium | The module shall support GET /api/agencies/{id}/employees to list active agency employees. | Endpoint integration test |
| RQ-5 | Functional | Medium | The module shall support GET /api/agencies to return the legacy complete agency list. | Endpoint integration test |
| RQ-6 | Functional | High | The module shall support POST /api/branches/agency/{agencyId} to add a branch to an agency. | Endpoint integration test |
| RQ-7 | Functional | Medium | The module shall support GET /api/branches to list every branch. | Endpoint integration test |
| RQ-8 | Functional | Medium | The module shall support GET /api/branches/agency/{agencyId} to list active branches for an agency. | Endpoint integration test |
| RQ-9 | Functional | Medium | The module shall support GET /api/branches/agency/{agencyId}/search to power the paginated remote branch selector. | Endpoint integration test |
| RQ-10 | Functional | Medium | The module shall support GET /api/branches/agency/{agencyId}/branch/{branchId}/employees to list branch employees after ownership validation. | Endpoint integration test |
| RQ-11 | Non-functional | Very High | The server shall enforce authentication, authorization, and ownership independently of client visibility. | Security integration test |
| RQ-12 | Non-functional | Very High | Multi-record state changes shall be transactional and rollback on failure. | Transactional integration test |
| RQ-13 | Non-functional | High | Failures shall use stable codes and user-readable messages without exposing stack traces. | Error-contract test |
| RQ-14 | Non-functional | Medium | Collection operations shall use bounded pagination, safe sorting, and explicit loading or empty states. | Pagination/UI test |
| RQ-15 | Non-functional | Medium | Important state transitions shall be observable through audit data or structured logs. | Audit/log verification |

## Priority definition

- Very High: security, money, booking integrity, inventory, or irreversible state.
- High: core business capability or mutation.
- Medium: read-only discovery, usability, observability, or operational convenience.

## Traceability

Each RQ maps to an endpoint/service function, one or more UC entries, and the related WF/FC processes.

