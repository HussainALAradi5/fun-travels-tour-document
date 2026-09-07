# UserRequestService

**File:** `src/main/java/com/server/server/services/UserRequestService.java`

## Methods

### create(UserRequest) -> UserRequest
Creates support request, notifies support agents.

### getRequests(FilterParams) -> Page<UserRequest>
Customers see own; support see assigned; admins see all.

### getById(id) -> UserRequest
### assignToAgent(requestId, agentId) -> UserRequest
### solveRequest(id, resolution) -> UserRequest
### rejectRequest(id, reason) -> UserRequest
### delete(id) -> void
