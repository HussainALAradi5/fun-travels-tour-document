# NotificationService

Source: `services/notification/NotificationService.java`.

## Functions

### `void sendUserRequestNotification(UserRequest request, NotificationType type)`

### `void sendNotification(User recipient, String title, String message, NotificationType type, Integer refId, ReferenceType refType)`

**Runs in:** transaction

### `Notification markAsRead(Integer notificationId)`

**Runs in:** transaction

### `void scheduleSevenDayReminders()`

**Runs in:** scheduled `cron = "0 0 9 * * ?"`

### `NotificationCounts getNotificationCounts(Integer userId)`

**Runs in:** read-only transaction

### `void sendTicketAutoCancellationNotification(Ticket ticket)`

### `void sendTourCompletionGreeting(Ticket ticket)`

### `List<Notification> filterUserNotifications(Integer userId, String search, Boolean isRead, NotificationType type, ReferenceType refType, LocalDate startDate, LocalDate endDate)`

**Runs in:** read-only transaction
