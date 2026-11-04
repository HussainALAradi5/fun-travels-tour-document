## Business logic

Stores generated files under the private `app.media-dir` (never served statically) at `reports/<ownerId>/<random>.<ext>`, with a `Media` record holding name, type, size, category, owner, report type and format, and row count. Only the owner or an administrator can download or delete a file (403 otherwise, 404 when missing). `listMine` returns the caller's files, newest first. Storage paths are never returned to clients, and `FileStorageService` rejects paths that would leave the media folder.
