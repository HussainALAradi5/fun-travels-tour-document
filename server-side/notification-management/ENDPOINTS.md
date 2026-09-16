# Notification Management Endpoints

This table is the feature-owned HTTP contract. Business rules and exception details are documented in this folder's service pages.

| ID | Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|---|
| EP-1 | `GET` | `/api/notifications/user/{userId}` | Show a user's notifications. | User ID | `NotificationService` | `getUserNotifications` |
| EP-2 | `PUT` | `/api/notifications/{id}/read` | Mark a notification read. | Notification ID | `NotificationService` | `markAsRead` |
| EP-3 | `GET` | `/api/notifications/user/{userId}/counts` | Show unread/total counters. | User ID | `NotificationService` | `getNotificationCounts` |

## Endpoint rules

- Authentication and role authorization are enforced by the server.
- Request validation occurs before business-state changes.
- Success and error responses use the shared API envelope.
- Collection endpoints use bounded pagination where supported.

