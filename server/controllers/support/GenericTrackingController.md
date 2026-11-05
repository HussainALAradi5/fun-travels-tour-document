# GenericTrackingController

Base path `/api/tracking`. Source: `controllers/support/GenericTrackingController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/tracking/{refType}/{refId}` | `GenericTrackingService.getTimeline` | Events and comments of one record, oldest first. | any signed-in user | - | `TimelineResponse` | 401, 403, 404 |
| `POST /api/tracking/{refType}/{refId}/comments` | `GenericTrackingService.addComment` | Add comment. | any signed-in user | body `CommentRequest` | `CommentResponse` | 400, 401, 403, 404, 409 |
| `PUT /api/tracking/comments/{commentId}` | `GenericTrackingService.updateComment` | Authors edit their own comments. | any signed-in user | body `CommentRequest` | `CommentResponse` | 400, 401, 403, 404, 409 |
