# UserRequestService

Source: `services/support/UserRequestService.java`.

## Functions

### `UserRequest create(UserRequestCreateRequest createRequest)`

**Runs in:** transaction

### `UserRequest assignRequest(Integer requestId, Integer agentId)`

**Runs in:** transaction; roles: ADMIN, SUPPORT_AGENT

### `UserRequest solveRequest(Integer requestId)`

**Runs in:** transaction

### `UserRequest rejectRequest(Integer requestId)`

**Runs in:** transaction; roles: ADMIN, SUPPORT_AGENT

### `PageResponse<UserRequest> getFilteredRequests(UserRequestFilterRequest filter)`

**Runs in:** read-only transaction

### `UserRequest getById(Integer id)`

### `void delete(Integer id)`
