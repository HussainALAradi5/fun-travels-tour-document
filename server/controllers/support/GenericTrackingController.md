# GenericTrackingController

Base path `/api/tracking`. Source: `controllers/support/GenericTrackingController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/tracking/{refType}/{refId}` | `GenericTrackingService.getTimeline` | Get timeline. | any signed-in user | - | `TimelineResponse` |
| `POST /api/tracking/{refType}/{refId}/comments` | `GenericTrackingService.addComment` | Add comment. | any signed-in user | body `CommentRequest` | `CommentResponse` |
| `PUT /api/tracking/comments/{commentId}` | `GenericTrackingService.updateComment` | Only the author edits a comment, and only while the record is still open. | any signed-in user | body `CommentRequest` | `CommentResponse` |
