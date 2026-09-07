# NotificationController

**File:** `src/main/java/com/server/server/controllers/NotificationController.java`
**Base Path:** `/api/notifications`

## Endpoints

### GET /api/notifications/user/{userId}

**Description:** Get user notifications with pagination
**Service Method:** `NotificationService.getUserNotifications(...)`
**Path Params:** userId (Integer)
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| type | NotificationType | No | Filter by type |
| isRead | Boolean | No | Filter by read status |
| startDate | LocalDate | No | Start date |
| endDate | LocalDate | No | End date |
| page | int | No | Page number (default: 0) |
| size | int | No | Page size (default: 20) |
**Response (200 OK):** Page of Notification entities
**Access:** Authenticated (own notifications)

---

### PUT /api/notifications/{id}/read

**Description:** Mark notification as read
**Service Method:** `NotificationService.markAsRead(id)`
**Path Params:** id (Integer)
**Response (200 OK):** Updated Notification
**Access:** Authenticated (own notifications)

---

### GET /api/notifications/counts/{userId}

**Description:** Get unread notification counts
**Service Method:** `NotificationService.getCounts(userId)`
**Path Params:** userId (Integer)
**Response (200 OK):** { unreadCount: number }
**Access:** Authenticated (own counts)
