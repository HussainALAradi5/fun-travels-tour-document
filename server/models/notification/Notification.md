# Notification

Table `notifications`. Inherits `BaseEntity`. Source: `models/notification/Notification.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `recipient` | `User` | ManyToOne  |
| `title` | `String` |  required |
| `message` | `String` |  required |
| `type` | `NotificationType` |  required |
| `isRead` | `Boolean` |  required |
| `referenceId` | `Integer` |   |
| `referenceType` | `ReferenceType` |   |
| `readAt` | `LocalDateTime` |   |
