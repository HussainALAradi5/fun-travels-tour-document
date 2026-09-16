# Support Management Client API Usage Endpoints

This table is the feature-owned HTTP contract. Business rules and exception details are documented in this folder's service pages.

| ID | Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|---|
| EP-1 | `POST` | `/api/user-requests` | Open a support request. | Validated `UserRequest` | `UserRequestService` | `create` |
| EP-2 | `GET` | `/api/user-requests` | Search support requests. | `UserRequestFilterRequest` | `UserRequestService` | `getFilteredRequests` |
| EP-3 | `GET` | `/api/user-requests/{id}` | View one request. | Request ID | `UserRequestService` | `getById` |
| EP-4 | `PATCH` | `/api/user-requests/{id}/assign/{agentId}` | Assign support ownership. | Request and agent IDs | `UserRequestService` | `assignRequest` |
| EP-5 | `PATCH` | `/api/user-requests/{id}/solve/{solverId}` | Resolve a support request. | Request and solver IDs | `UserRequestService` | `solveRequest` |
| EP-6 | `PATCH` | `/api/user-requests/{id}/reject/{rejectedById}` | Reject a support request. | Request and actor IDs | `UserRequestService` | `rejectRequest` |
| EP-7 | `DELETE` | `/api/user-requests/{id}` | Delete an eligible request. | Request ID | `UserRequestService` | `delete` |
| EP-8 | `GET` | `/api/tracking/{refType}/{refId}` | Read comments and event history for a domain record. | Reference type and ID | `GenericTrackingService` | `getTimelineMap` |
| EP-9 | `POST` | `/api/tracking/{refType}/{refId}/comments` | Add an auditable comment. | Reference, content, user ID | `GenericTrackingService` | `addComment` |
| EP-10 | `PUT` | `/api/tracking/comments/{commentId}` | Edit the author's comment. | Comment ID, editor ID, content | `GenericTrackingService` | `updateComment` |

## Endpoint rules

- Authentication and role authorization are enforced by the server.
- Request validation occurs before business-state changes.
- Success and error responses use the shared API envelope.
- Collection endpoints use bounded pagination where supported.

