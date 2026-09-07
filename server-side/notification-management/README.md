# Notification Management

Real-time notification system with WebSocket push and REST queries.

## Entities
- **Notification** - User notification with type, read status, and entity reference

## Services
- [NotificationService](services/NotificationService.md) - Notification CRUD and WebSocket push

## Endpoints
- [NotificationController](endpoints/NotificationController.md) - `/api/notifications`

## Business Logic
- Notifications are pushed in real-time via WebSocket (STOMP)
- WebSocket endpoint: /ws-notifications, topic: /topic/notifications/{userId}
- Notifications reference entities (tour, reservation, ticket, user request)
