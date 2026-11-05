# TourStatusService

Source: `services/tourmanagement/TourStatusService.java`.

Tour status workflow (PENDING -> APPROVED -> ACTIVE -> COMPLETED, or CANCELLED) and its effects on bookings.

## Business logic

Status workflow: PENDING -> APPROVED or CANCELLED; APPROVED -> ACTIVE or CANCELLED; ACTIVE -> COMPLETED or CANCELLED; CANCELLED -> PENDING. Only people who may manage the tour can change it (see TourService). Going ACTIVE opens all places for booking. Cancellation requires at least 14 days to departure and no more than one third of capacity booked; every active booking is then cancelled and paid tickets are fully refunded.

## Functions

### `Tour updateStatus(Integer id, GenericStatus newStatus)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Cannot change the status of a completed tour. | `WorkflowException` | 409 |
| A cancelled tour can only be restored to PENDING status. | `WorkflowException` | 409 |
| Cancellation denied: Tour is less than 2 weeks away. | `WorkflowException` | 409 |
| Cancellation denied: Booked seats exceed 1/3 of total capacity. | `WorkflowException` | 409 |
| A pending tour must be APPROVED or CANCELLED. | `WorkflowException` | 409 |
| An approved tour must be made ACTIVE or CANCELLED. | `WorkflowException` | 409 |
| An active tour must be marked COMPLETED or CANCELLED. | `WorkflowException` | 409 |
| Status change not allowed by the workflow | `WorkflowException` | 409 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
