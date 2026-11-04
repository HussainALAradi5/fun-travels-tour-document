# MediaController

Base path `/api/media`. Source: `controllers/media/MediaController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/media` | `MediaService.listMine` | The caller's own files, newest first. | any signed-in user | query `category`, `page`, `size` | `PageResponse<MediaResponse>` |
| `GET /api/media/{id}/download` | `MediaService.open` | Streams a file to its owner or an administrator. | any signed-in user | - | `byte[]` |
| `DELETE /api/media/{id}` | `MediaService.delete` | Delete. | any signed-in user | - | `Void` |
