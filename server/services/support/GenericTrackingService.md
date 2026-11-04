# GenericTrackingService

Source: `services/support/GenericTrackingService.java`.

Comments and event logs attached to any record type, with per-type access rules.

## Business logic

Timelines (events + comments) are readable only by people who can read the record: user requests (requester or support staff), reservations and tickets (owner customer or same-agency staff), tours (staff of the tour's agency), users (self or admin). Closed user requests accept no new comments; only the author edits a comment.

## Functions

### `TimelineResponse getTimeline(Integer refId, ReferenceType refType)`

**Runs in:** read-only transaction

### `GenericComment addComment(Integer refId, ReferenceType refType, String content)`

**Runs in:** transaction

### `GenericComment updateComment(Integer commentId, String newContent)`

**Purpose:** Only the author edits a comment, and only while the record is still open.

**Runs in:** transaction

### `void logEvent(Integer refId, ReferenceType refType, String action, String description, User actor)`

**Runs in:** transaction
