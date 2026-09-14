# NotificationService

## Complete function reference

| Function and signature | Parameters | Logic and business purpose | Return / side effects | Exceptions |
|---|---|---|---|---|
| `public void sendUserRequestNotification(UserRequest request, NotificationType type)` | Request and event type | Selects recipients/title/message for the support event and delegates notification creation. | Writes notifications. | Missing relationship/persistence failures may propagate. |
| `public void sendNotification(User recipient, String title, String message, NotificationType type, Integer refId, ReferenceType refType)` | Recipient, presentation, type, optional reference | Builds and persists one domain-linked notification. | Writes notification. | Persistence failures may propagate. |
| `public List<Notification> getUserNotifications(Integer userId)` | Required user ID | Loads the user's notification stream. | Notification list; read-only. | Null ID validation. |
| `public Notification markAsRead(Integer notificationId)` | Required notification ID | Resolves notification, marks read, and saves. | Updated notification. | Missing notification failure propagates. |
| `public void scheduleSevenDayReminders()` | None | Finds eligible future travel and emits reminder notifications on schedule. | Writes reminders. | Individual processing failures follow scheduler logging behavior. |
| `public NotificationCounts getNotificationCounts(Integer userId)` | Required user ID | Aggregates total and unread counts. | Count DTO; read-only. | Null ID validation. |
| `public void sendTicketAutoCancellationNotification(Ticket ticket)` | Cancelled ticket | Formats and sends an automatic cancellation alert. | Writes notification. | Missing recipient/persistence failures may propagate. |
| `public void sendTourCompletionGreeting(Ticket ticket)` | Completed-tour ticket | Formats and sends post-tour greeting. | Writes notification. | Missing recipient/persistence failures may propagate. |
| `public List<Notification> filterUserNotifications(...)` | User and optional type/read/date criteria | Builds repository filters and returns matching notifications. | Filtered list; read-only. | Invalid criteria/repository failures may propagate. |

**File:** `src/main/java/com/server/server/services/NotificationService.java`

## Methods

### getUserNotifications(userId, type, isRead, startDate, endDate, page, size) -> Page<Notification>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| userId | Integer | User ID |
| type | NotificationType | Filter by type |
| isRead | Boolean | Filter by read status |
| startDate | LocalDate | Start date |
| endDate | LocalDate | End date |
| page | int | Page number |
| size | int | Page size |

**Returns:** Paginated notifications

---

### markAsRead(id) -> Notification

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Notification ID |

**Returns:** Updated Notification

**Business Logic:** Sets isRead = true

---

### getCounts(userId) -> Map<String, Object>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| userId | Integer | User ID |

**Returns:** Map with unread count

---

### sendNotification(recipient, type, title, message, refType, refId) -> Notification

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| recipient | User | Notification recipient |
| type | NotificationType | Notification type |
| title | String | Notification title |
| message | String | Notification body |
| refType | ReferenceType | Optional entity type |
| refId | Long | Optional entity ID |

**Returns:** Created Notification

**Business Logic:**
1. Creates Notification record
2. Pushes via WebSocket to `/topic/notifications/{userId}`
