# NotificationController

**File:** `src/main/java/com/server/server/controllers/NotificationController.java`
**Base Path:** `/api/notifications`

## Endpoints

### GET /api/notifications/user/{userId}
Get user notifications with pagination.
**Access:** Authenticated (own)

### PATCH /api/notifications/{id}/read
Mark notification as read.
**Access:** Authenticated (own)

### GET /api/notifications/counts/{userId}
Get unread notification counts.
**Access:** Authenticated (own)

## WebSocket
- Endpoint: /ws-notifications (STOMP)
- Subscribe: /topic/notifications/{userId}
