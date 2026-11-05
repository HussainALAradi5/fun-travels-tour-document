# GenericTrackingService

Source: `services/support/GenericTrackingService.java`.

Comments and event logs attached to any record type, with per-type access rules.

## Business logic

Timelines (events + comments) are readable only by people who can read the record: user requests (requester or support staff), reservations and tickets (owner customer or same-agency staff), tours (staff of the tour's agency), users (self or admin). Closed user requests accept no new comments; only the author edits a comment.

## Functions

### `TimelineResponse getTimeline(Integer refId, ReferenceType refType)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| You are not allowed to access this request timeline. | `AccessDeniedException` | 403 |
| Reservation not found | `ResourceNotFoundException` | 404 |
| Ticket not found | `ResourceNotFoundException` | 404 |
| Tour timelines are only available to staff. | `AccessDeniedException` | 403 |
| Tour not found | `ResourceNotFoundException` | 404 |
| You are not allowed to access this timeline. | `AccessDeniedException` | 403 |
| Request not found | `ResourceNotFoundException` | 404 |

### `GenericComment addComment(Integer refId, ReferenceType refType, String content)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Comment content is required. | `IllegalArgumentException` | 400 |
| This request is closed. No further modifications are allowed. | `WorkflowException` `REQUEST_CLOSED` | 409 |
| Request not found | `ResourceNotFoundException` | 404 |
| You are not allowed to access this request timeline. | `AccessDeniedException` | 403 |
| Reservation not found | `ResourceNotFoundException` | 404 |
| Ticket not found | `ResourceNotFoundException` | 404 |
| Tour timelines are only available to staff. | `AccessDeniedException` | 403 |
| Tour not found | `ResourceNotFoundException` | 404 |
| You are not allowed to access this timeline. | `AccessDeniedException` | 403 |

### `GenericComment updateComment(Integer commentId, String newContent)`

**Purpose:** Only the author edits a comment, and only while the record is still open.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Comment not found | `ResourceNotFoundException` | 404 |
| Only the author can edit this comment. | `AccessDeniedException` | 403 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Comment content is required. | `IllegalArgumentException` | 400 |
| This request is closed. No further modifications are allowed. | `WorkflowException` `REQUEST_CLOSED` | 409 |
| Request not found | `ResourceNotFoundException` | 404 |
| You are not allowed to access this request timeline. | `AccessDeniedException` | 403 |
| Reservation not found | `ResourceNotFoundException` | 404 |
| Ticket not found | `ResourceNotFoundException` | 404 |
| Tour timelines are only available to staff. | `AccessDeniedException` | 403 |
| Tour not found | `ResourceNotFoundException` | 404 |
| You are not allowed to access this timeline. | `AccessDeniedException` | 403 |

### `void logEvent(Integer refId, ReferenceType refType, String action, String description, User actor)`

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.
