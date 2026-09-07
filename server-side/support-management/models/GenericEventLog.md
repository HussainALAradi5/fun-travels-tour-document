# GenericEventLog Model

**Table:** `generic_event_logs`
**File:** `src/main/java/com/server/server/Models/GenericEventLog.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| referenceType | String | Not Blank | Entity type name |
| referenceId | Long | Not Null | Entity ID |
| eventType | String | Not Blank | Event type (STATUS_CHANGE, UPDATE, etc.) |
| description | String | - | Event description |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| actor | User | ManyToOne | User who performed action |
