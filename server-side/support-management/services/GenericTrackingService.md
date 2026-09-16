# GenericTrackingService

## Complete function reference

| Function and signature | Parameters | Logic and business purpose | Return / side effects | Exceptions |
|---|---|---|---|---|
| `public Map<String,Object> getTimelineMap(Integer refId, ReferenceType refType)` | Required reference ID/type | Combines comments and events into one auditable timeline response. | Timeline map; read-only. | Reference validation failures may propagate. |
| `public GenericComment addComment(Integer refId, ReferenceType refType, String content, Integer userId)` | Reference, text, author ID | Validates modifiability, resolves author, saves comment, and logs the event. | Created comment and audit event. | Closed reference: `"This request is closed. No further modifications are allowed."`; missing user/reference errors propagate. |
| `public GenericComment updateComment(Integer commentId, Integer editorId, String newContent)` | Comment, editor, new text | Resolves comment and editor, verifies authorship, updates text/time, and saves. | Updated comment. | `"Unauthorized: Only the author can edit this comment"`; missing resources propagate. |
| `public List<GenericComment> getComments(Integer refId, ReferenceType refType)` | Reference ID/type | Queries comments in timeline order. | Comment list; read-only. | Repository failures may propagate. |
| `public void logEvent(Integer refId, ReferenceType refType, String action, String description, User actor)` | Reference and event metadata | Constructs and saves an immutable audit event. | Writes event log. | Persistence failures may propagate. |
| `public List<GenericEventLog> getEvents(Integer refId, ReferenceType refType)` | Reference ID/type | Queries event history. | Event list; read-only. | Repository failures may propagate. |

**File:** `src/main/java/com/server/server/services/GenericTrackingService.java`

## Methods

### getTimeline(refType, refId) -> TimelineItem[]
Merged event log + comments timeline.

### addComment(refType, refId, content) -> GenericComment
### updateComment(commentId, content) -> GenericComment

## Detailed behavior and displayed errors

### `getTimelineMap(Integer refId, ReferenceType refType)`

Loads comments and event records for the same reference and returns the data required to render one auditable timeline. It is read-only and must not silently mix different reference types. Invalid/missing references display their resource-specific validation message.

### `addComment(Integer refId, ReferenceType refType, String content, Integer userId)`

Verifies that the referenced workflow is still modifiable, resolves the author, saves the comment, and records a matching audit event. Both records should be committed as one operation. A closed workflow displays `This request is closed. No further modifications are allowed.` A missing author or reference displays its resource-not-found message. Empty content should be rejected with a `content` field error.

### `updateComment(Integer commentId, Integer editorId, String newContent)`

Loads the comment and editor, verifies that the editor is the original author, updates the text and modification time, and saves. A different user receives `Unauthorized: Only the author can edit this comment`. Missing records use their resource-not-found messages. Empty replacement content should be rejected before persistence.

### `getComments(...)` and `getEvents(...)`

Return the ordered comment or audit history for exactly one reference. They are read-only. Unexpected repository failures are represented by the safe generic API error rather than persistence details.

### `logEvent(...)`

Creates an immutable event describing the action, actor, target reference, and description. Events are appended; existing audit history is not edited. Persistence failures roll back the calling transactional workflow when invoked inside it.
