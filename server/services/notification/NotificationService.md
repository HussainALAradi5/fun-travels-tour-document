# NotificationService

Source: `services/notification/NotificationService.java`.

## Functions

### `void sendUserRequestNotification(UserRequest request, NotificationType type)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `void sendNotification(User recipient, String title, String message, NotificationType type, Integer refId, ReferenceType refType)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| User not found | `ResourceNotFoundException` | 404 |

### `Notification markAsRead(Integer notificationId)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Notification not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `void scheduleSevenDayReminders()`

**Runs in:** read-only transaction; scheduled `cron = "0 0 9 * * ?"`

**Exceptions:** none of its own; failures come from the functions it calls.

### `NotificationCounts getNotificationCounts(Integer userId)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `void sendTicketAutoCancellationNotification(Ticket ticket)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `void sendTourCompletionGreeting(Ticket ticket)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `List<Notification> filterUserNotifications(Integer userId, String search, Boolean isRead, NotificationType type, ReferenceType refType, LocalDate startDate, LocalDate endDate)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.
