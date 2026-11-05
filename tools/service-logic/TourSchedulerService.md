## Business logic

Nightly (`autoProcessScheduledTours`, registered with `SystemSchedulingService`): PENDING tours past their start date are cancelled; ACTIVE/APPROVED tours past their end date are completed, their tickets completed, and each traveler greeted once. Every step is logged on the tour's timeline.
