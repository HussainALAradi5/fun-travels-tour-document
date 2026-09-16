# User Management Requirements

## Requirement catalog

| ID | Type | Priority | Requirement | Verification |
|---|---|---|---|---|
| RQ-1 | Functional | Very High | The module shall support POST /api/auth/register to create a customer account. | Endpoint integration test |
| RQ-2 | Functional | Very High | The module shall support POST /api/auth/login to authenticate and issue a JWT. | Endpoint integration test |
| RQ-3 | Functional | Medium | The module shall support GET /api/users to list users for administration. | Endpoint integration test |
| RQ-4 | Functional | Medium | The module shall support GET /api/users/{id} to view one user. | Endpoint integration test |
| RQ-5 | Functional | Medium | The module shall support GET /api/users/agency/{agencyId} to list agency staff, optionally by role. | Endpoint integration test |
| RQ-6 | Functional | High | The module shall support PUT /api/users/{id} to update a user profile. | Endpoint integration test |
| RQ-7 | Functional | High | The module shall support POST /api/users/bulk-import to import multiple employees. | Endpoint integration test |
| RQ-8 | Functional | High | The module shall support PUT /api/users/permissions/{id} to change role and branch assignment. | Endpoint integration test |
| RQ-9 | Functional | High | The module shall support POST /api/users/add-employee to create an employee account. | Endpoint integration test |
| RQ-10 | Functional | High | The module shall support DELETE /api/users/{id} to deactivate a user without deleting history. | Endpoint integration test |
| RQ-11 | Functional | Medium | The module shall support GET /api/users/role/{type} to find users by application role. | Endpoint integration test |
| RQ-12 | Functional | High | The module shall support POST /api/users/request-password-reset to send a reset link. | Endpoint integration test |
| RQ-13 | Functional | High | The module shall support POST /api/users/confirm-password-reset to consume a reset token and set a password. | Endpoint integration test |
| RQ-14 | Functional | Medium | The module shall support GET /api/accounts/user/{userId}/balance to show wallet/account balance. | Endpoint integration test |
| RQ-15 | Functional | Medium | The module shall support GET /api/accounts/user/{userId}/history to show wallet transaction history. | Endpoint integration test |
| RQ-16 | Non-functional | Very High | The server shall enforce authentication, authorization, and ownership independently of client visibility. | Security integration test |
| RQ-17 | Non-functional | Very High | Multi-record state changes shall be transactional and rollback on failure. | Transactional integration test |
| RQ-18 | Non-functional | High | Failures shall use stable codes and user-readable messages without exposing stack traces. | Error-contract test |
| RQ-19 | Non-functional | Medium | Collection operations shall use bounded pagination, safe sorting, and explicit loading or empty states. | Pagination/UI test |
| RQ-20 | Non-functional | Medium | Important state transitions shall be observable through audit data or structured logs. | Audit/log verification |

## Priority definition

- Very High: security, money, booking integrity, inventory, or irreversible state.
- High: core business capability or mutation.
- Medium: read-only discovery, usability, observability, or operational convenience.

## Traceability

Each RQ maps to an endpoint/service function, one or more UC entries, and the related WF/FC processes.

