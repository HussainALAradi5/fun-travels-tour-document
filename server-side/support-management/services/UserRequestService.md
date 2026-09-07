# UserRequestService

**File:** `src/main/java/com/server/server/services/UserRequestService.java`

## Methods

### create(UserRequest) -> UserRequest

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| request | UserRequest | Request entity with subject, description, requestType |

**Returns:** Created UserRequest

**Business Logic:**
1. Sets status to PENDING
2. Sends notification to support agents
3. Logs creation event

---

### getRequests(status, type, submitterId, page, size) -> Page<UserRequest>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| status | UserRequestStatus | Filter by status |
| type | UserRequestType | Filter by type |
| submitterId | Integer | Filter by submitter |
| page | int | Page number |
| size | int | Page size |

**Returns:** Paginated requests

**Business Logic:**
- Customers see only their own requests
- Support agents see assigned and unassigned
- Admins see all

---

### assignToAgent(requestId, agentId) -> UserRequest

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| requestId | Integer | Request ID |
| agentId | Integer | Support agent user ID |

**Returns:** Updated UserRequest

**Business Logic:**
1. Validates agent has SUPPORT_AGENT role
2. Sets assignedTo
3. Sends notification to agent

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | Agent not found or not SUPPORT_AGENT |

---

### solveRequest(id, resolution) -> UserRequest

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Request ID |
| resolution | String | Resolution description |

**Returns:** Updated UserRequest

**Business Logic:**
1. Sets status to SOLVED
2. Sets resolution text
3. Sets solvedBy to current user
4. Sends notification to submitter

---

### rejectRequest(id, reason) -> UserRequest

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Request ID |
| reason | String | Rejection reason |

**Returns:** Updated UserRequest

**Business Logic:**
1. Sets status to REJECTED
2. Sets resolution to reason
3. Sends notification to submitter
