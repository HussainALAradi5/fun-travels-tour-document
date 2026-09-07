# Notification Model

**Table:** `notifications`
**File:** `src/main/java/com/server/server/Models/Notification.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| title | String | Not Blank | Notification title |
| message | String | Not Blank | Notification body |
| notificationType | NotificationType | Not Null | Type of notification |
| referenceType | ReferenceType | - | Related entity type |
| referenceId | Long | - | Related entity ID |
| isRead | boolean | Default: false | Read status |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| recipient | User | ManyToOne | Notification recipient |
