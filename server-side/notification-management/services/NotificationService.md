# NotificationService

**File:** `src/main/java/com/server/server/services/NotificationService.java`

## Methods

### getUserNotifications(userId, filters) -> Page<Notification>
### markAsRead(id) -> Notification
### getCounts(userId) -> NotificationCounts
### sendNotification(recipient, type, title, message, refType?, refId?) -> Notification
Creates record and pushes via WebSocket.

### sendWebSocketNotification(userId, notification) -> void
Push via WebSocket only (no database record).
