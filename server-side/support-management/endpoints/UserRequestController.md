# UserRequestController

**File:** `src/main/java/com/server/server/controllers/UserRequestController.java`
**Base Path:** `/api/requests`

## Endpoints

### POST /api/requests

**Description:** Create a support request
**Service Method:** `UserRequestService.create(request)`
**Request Body:**
```json
{
  "subject": "string",
  "description": "string",
  "requestType": "SUPPORT"
}
```
**Response (200 OK):** Created UserRequest
**Access:** Authenticated

---

### GET /api/requests

**Description:** Get requests with pagination
**Service Method:** `UserRequestService.getRequests(...)`
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| status | UserRequestStatus | No | Filter by status |
| type | UserRequestType | No | Filter by type |
| submitterId | Integer | No | Filter by submitter |
| page | int | No | Page number |
| size | int | No | Page size |
**Response (200 OK):** Page of UserRequest
**Access:** Authenticated (filtered by role)

---

### GET /api/requests/{id}

**Description:** Get request by ID
**Service Method:** `UserRequestService.getById(id)`
**Response (200 OK):** UserRequest entity
**Access:** Authenticated (own or admin/support)

---

### PATCH /api/requests/{id}/assign

**Description:** Assign request to support agent
**Service Method:** `UserRequestService.assignToAgent(requestId, agentId)`
**Request Body:**
```json
{
  "agentId": 5
}
```
**Response (200 OK):** Updated UserRequest
**Access:** ADMIN, SUPPORT_AGENT

---

### PATCH /api/requests/{id}/solve

**Description:** Mark request as solved
**Service Method:** `UserRequestService.solveRequest(id, resolution)`
**Request Body:**
```json
{
  "resolution": "Issue resolved"
}
```
**Response (200 OK):** Updated UserRequest
**Access:** ADMIN, SUPPORT_AGENT

---

### PATCH /api/requests/{id}/reject

**Description:** Reject request
**Service Method:** `UserRequestService.rejectRequest(id, reason)`
**Request Body:**
```json
{
  "reason": "Not applicable"
}
```
**Response (200 OK):** Updated UserRequest
**Access:** ADMIN, SUPPORT_AGENT

---

### DELETE /api/requests/{id}

**Description:** Delete request
**Service Method:** `UserRequestService.delete(id)`
**Access:** ADMIN
