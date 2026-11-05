# MediaController

Base path `/api/media`. Source: `controllers/media/MediaController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/media` | `MediaService.listMine` | The caller's own files, newest first. | any signed-in user | query `category`, `page`, `size` | `PageResponse<MediaResponse>` | 400, 401, 403 |
| `GET /api/media/{id}/download` | `MediaService.open` | Streams a file to its owner or an administrator. | any signed-in user | - | `byte[]` | 401, 403, 404 |
| `DELETE /api/media/{id}` | `MediaService.delete` | Delete. | any signed-in user | - | `Void` | 401, 403, 404 |
