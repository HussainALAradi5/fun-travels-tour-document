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
