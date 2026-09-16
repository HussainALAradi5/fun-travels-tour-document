# Support Management Requirements

## Requirement catalog

| ID | Type | Priority | Requirement | Verification |
|---|---|---|---|---|
| RQ-1 | Functional | High | The module shall support POST /api/user-requests to open a support request. | Endpoint integration test |
| RQ-2 | Functional | Medium | The module shall support GET /api/user-requests to search support requests. | Endpoint integration test |
| RQ-3 | Functional | Medium | The module shall support GET /api/user-requests/{id} to view one request. | Endpoint integration test |
| RQ-4 | Functional | High | The module shall support PATCH /api/user-requests/{id}/assign/{agentId} to assign support ownership. | Endpoint integration test |
| RQ-5 | Functional | High | The module shall allow only the requester, assigned agent, support agent, or administrator to complete an assigned request, and shall derive the actor from authentication. | Authorization and workflow integration test |
| RQ-6 | Functional | High | The module shall allow only support agents or administrators to reject pending or assigned requests, and shall derive the actor from authentication. | Authorization and workflow integration test |
| RQ-7 | Functional | High | The module shall support DELETE /api/user-requests/{id} to delete an eligible request. | Endpoint integration test |
| RQ-8 | Functional | Medium | The module shall support GET /api/tracking/{refType}/{refId} to read comments and event history for a domain record. | Endpoint integration test |
| RQ-9 | Functional | High | The module shall support POST /api/tracking/{refType}/{refId}/comments to add an auditable comment. | Endpoint integration test |
| RQ-10 | Functional | High | The module shall support PUT /api/tracking/comments/{commentId} to edit the author's comment. | Endpoint integration test |
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
