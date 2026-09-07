# Support Management

Handles support requests, comments, and audit trail logging.

## Entities
- **UserRequest** - Support/suggestion ticket from users
- **GenericComment** - Polymorphic comment on any entity
- **GenericEventLog** - Audit trail for entity changes

## Services
- [UserRequestService](services/UserRequestService.md) - Support ticket lifecycle
- [GenericTrackingService](services/GenericTrackingService.md) - Comments and event logs

## Endpoints
- [UserRequestController](endpoints/UserRequestController.md) - `/api/requests`
- [GenericTrackingController](endpoints/GenericTrackingController.md) - `/api/tracking`

## Business Logic
- Support requests follow: PENDING -> ASSIGNED -> SOLVED/REJECTED
- Comments are polymorphic (attach to any entity by type+id)
- Timeline merges comments and events chronologically
