# TourSchedulerService

Source: `services/tourmanagement/TourSchedulerService.java`.

Nightly tour housekeeping: cancels PENDING tours whose start date passed and completes finished ACTIVE tours.

## Business logic

Nightly (`autoProcessScheduledTours`, registered with `SystemSchedulingService`): PENDING tours past their start date are cancelled; ACTIVE/APPROVED tours past their end date are completed, their tickets completed, and each traveler greeted once. Every step is logged on the tour's timeline.

## Functions

### `void init()`

**Exceptions:** none of its own; failures come from the functions it calls.

### `void autoProcessScheduledTours()`

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.
