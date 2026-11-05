# UserRequestService

Source: `services/support/UserRequestService.java`.

## Functions

### `UserRequest create(UserRequestCreateRequest createRequest)`

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `UserRequest assignRequest(Integer requestId, Integer agentId)`

**Runs in:** transaction; roles: ADMIN, SUPPORT_AGENT

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Only a pending request can be assigned. | `IllegalStateException` | 409 |
| User not found | `ResourceNotFoundException` | 404 |
| Requests can only be assigned to a support agent or administrator. | `IllegalArgumentException` | 400 |
| Request not found | `ResourceNotFoundException` | 404 |
| You are not allowed to view this request. | `AccessDeniedException` | 403 |

### `UserRequest solveRequest(Integer requestId)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| You are not allowed to complete this request. | `AccessDeniedException` | 403 |
| Only an assigned request can be completed. | `IllegalStateException` | 409 |
| Request not found | `ResourceNotFoundException` | 404 |
| You are not allowed to view this request. | `AccessDeniedException` | 403 |

### `UserRequest rejectRequest(Integer requestId)`

**Runs in:** transaction; roles: ADMIN, SUPPORT_AGENT

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Only a pending or assigned request can be rejected. | `IllegalStateException` | 409 |
| Request not found | `ResourceNotFoundException` | 404 |
| You are not allowed to view this request. | `AccessDeniedException` | 403 |

### `PageResponse<UserRequest> getFilteredRequests(UserRequestFilterRequest filter)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `UserRequest getById(Integer id)`

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Request not found | `ResourceNotFoundException` | 404 |
| You are not allowed to view this request. | `AccessDeniedException` | 403 |

### `void delete(Integer id)`

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Only a pending request can be deleted by its requester. | `AccessDeniedException` | 403 |
| Request not found | `ResourceNotFoundException` | 404 |
| You are not allowed to view this request. | `AccessDeniedException` | 403 |
