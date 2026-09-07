# UserRequest Model

**Table:** `user_requests`
**File:** `src/main/java/com/server/server/Models/UserRequest.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| subject | String | Not Blank | Request subject |
| description | String | Not Blank | Request details |
| requestType | UserRequestType | Not Null | SUPPORT, SUGGESTION |
| status | UserRequestStatus | Not Null | Workflow status |
| resolution | String | - | Resolution notes |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| submitter | User | ManyToOne | Request creator |
| assignedTo | User | ManyToOne | Assigned support agent |
| solvedBy | User | ManyToOne | Resolving agent |
