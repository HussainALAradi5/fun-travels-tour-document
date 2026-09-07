# NotificationService

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
