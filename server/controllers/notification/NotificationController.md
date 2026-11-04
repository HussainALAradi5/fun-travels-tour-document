# NotificationController

Base path `/api/notifications`. Source: `controllers/notification/NotificationController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/notifications/user/{userId}` | `NotificationService.filterUserNotifications` | Get user notifications. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `search`, `isRead`, `type`, `refType`, `startDate`, `endDate` | `List<NotificationResponse>` |
| `PUT /api/notifications/{id}/read` | `NotificationService.markAsRead` | Mark as read. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `NotificationResponse` |
| `GET /api/notifications/user/{userId}/counts` | `NotificationService.getNotificationCounts` | Get notification counts. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `NotificationCounts` |
