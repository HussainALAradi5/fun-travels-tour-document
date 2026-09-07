# GenericTrackingController

**File:** `src/main/java/com/server/server/controllers/GenericTrackingController.java`
**Base Path:** `/api/tracking`

## Endpoints

### GET /api/tracking/timeline
Get merged timeline for an entity.
**Query Params:** refType, refId
**Access:** Authenticated

### POST /api/tracking/comment
Add comment to entity.
**Body:** { refType, refId, content }
**Access:** Authenticated

### PUT /api/tracking/comment/{commentId}
Update existing comment.
**Access:** Authenticated (author only)
