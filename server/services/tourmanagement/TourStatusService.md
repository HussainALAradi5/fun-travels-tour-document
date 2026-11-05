# TourStatusService

Source: `services/tourmanagement/TourStatusService.java`.

Tour status workflow (PENDING -> APPROVED -> ACTIVE -> COMPLETED, or CANCELLED) and its effects on bookings.

## Business logic

Status workflow: PENDING -> APPROVED or CANCELLED; APPROVED -> ACTIVE or CANCELLED; ACTIVE -> COMPLETED or CANCELLED; CANCELLED -> PENDING. Only people who may manage the tour can change it (see TourService). Going ACTIVE opens all places for booking. Cancellation requires at least 14 days to departure and no more than one third of capacity booked; every active booking is then cancelled and paid tickets are fully refunded.

## Functions

### `Tour updateStatus(Integer id, GenericStatus newStatus)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER
