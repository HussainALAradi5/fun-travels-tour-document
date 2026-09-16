# Payment Management Requirements

## Requirement catalog

| ID | Type | Priority | Requirement | Verification |
|---|---|---|---|---|
| RQ-1 | Functional | Very High | The module shall support GET /api/wallet/config to supply publishable payment configuration. | Endpoint integration test |
| RQ-2 | Functional | Very High | The module shall support POST /api/wallet/top-up to add externally paid funds to a wallet. | Endpoint integration test |
| RQ-3 | Functional | Very High | The module shall support POST /api/payments/execute/{reservationId} to pay and finalize a held reservation. | Endpoint integration test |
| RQ-4 | Functional | Very High | The module shall support GET /api/payments to search payments by owner, status, method, or dates. | Endpoint integration test |
| RQ-5 | Functional | Very High | The module shall support GET /api/payments/{id} to view one authorized payment. | Endpoint integration test |
| RQ-6 | Functional | Medium | The module shall support GET /api/transactions to search account transactions. | Endpoint integration test |
| RQ-7 | Functional | Medium | The module shall support GET /api/transactions/{id} to view one authorized transaction. | Endpoint integration test |
| RQ-8 | Functional | High | The module shall support POST /api/transactions/manual-credit/{userId} to apply an administrative wallet credit. | Endpoint integration test |
| RQ-9 | Non-functional | Very High | The server shall enforce authentication, authorization, and ownership independently of client visibility. | Security integration test |
| RQ-10 | Non-functional | Very High | Multi-record state changes shall be transactional and rollback on failure. | Transactional integration test |
| RQ-11 | Non-functional | High | Failures shall use stable codes and user-readable messages without exposing stack traces. | Error-contract test |
| RQ-12 | Non-functional | Medium | Collection operations shall use bounded pagination, safe sorting, and explicit loading or empty states. | Pagination/UI test |
| RQ-13 | Non-functional | Medium | Important state transitions shall be observable through audit data or structured logs. | Audit/log verification |

## Priority definition

- Very High: security, money, booking integrity, inventory, or irreversible state.
- High: core business capability or mutation.
- Medium: read-only discovery, usability, observability, or operational convenience.

## Traceability

Each RQ maps to an endpoint/service function, one or more UC entries, and the related WF/FC processes.

