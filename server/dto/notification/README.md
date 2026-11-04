# notification DTOs

Source: `dto/notification/`. Clients mirror these in `src/dtos/notification/`.

## NotificationCounts

response record.

| Field | Type | Rules |
| --- | --- | --- |
| `unreadCount` | `long` | - |

## NotificationResponse

response record; built by `from(Notification)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `title` | `String` | - |
| `message` | `String` | - |
| `type` | `NotificationType` | - |
| `referenceType` | `ReferenceType` | - |
| `referenceId` | `Integer` | - |
| `isRead` | `Boolean` | - |
| `createdAt` | `LocalDateTime` | - |
| `readAt` | `LocalDateTime` | - |
