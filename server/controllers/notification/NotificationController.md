# NotificationController

Base path `/api/v1/notifications`. Source: `controllers/notification/NotificationController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/v1/notifications/user/{userId}` | `NotificationService.filterUserNotifications` | Get user notifications. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | query `search`, `isRead`, `type`, `refType`, `startDate`, `endDate` | `List<NotificationResponse>` | 400, 401, 403 |
| `PUT /api/v1/notifications/{id}/read` | `NotificationService.markAsRead` | Mark as read. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `NotificationResponse` | 401, 403, 404 |
| `GET /api/v1/notifications/user/{userId}/counts` | `NotificationService.getNotificationCounts` | Get notification counts. | CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER (URL rule) | - | `NotificationCounts` | 401, 403 |
