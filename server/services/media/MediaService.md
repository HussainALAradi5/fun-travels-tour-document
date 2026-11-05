# MediaService

Source: `services/media/MediaService.java`.

Stored files and who may see them: the owner, or an administrator.

## Business logic

Stores generated files under the private `app.media-dir` (never served statically) at `reports/<ownerId>/<random>.<ext>`, with a `Media` record holding name, type, size, category, owner, report type and format, and row count. Only the owner or an administrator can download or delete a file (403 otherwise, 404 when missing). `listMine` returns the caller's files, newest first. Every night, reports older than `app.report-retention-days` (default 30) are deleted with their files. Storage paths are never returned to clients, and `FileStorageService` rejects paths that would leave the media folder.

## Functions

### `int deleteExpiredReports()`

**Purpose:** Nightly: removes reports older than `app.report-retention-days`, files and records.

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `Media storeReport(byte[] content, String fileName, ReportType type, ReportFormat format, int recordCount, User owner)`

**Purpose:** Saves a generated report for its owner under `reports/<ownerId>/<random>.<ext>`.

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `PageResponse<Media> listMine(MediaCategory category, Integer page, Integer size)`

**Purpose:** The signed-in user's files, newest first, optionally of one category.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `MediaFile open(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Media not found | `ResourceNotFoundException` | 404 |
| You can only access your own files. | `AccessDeniedException` | 403 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `void delete(Integer id)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Media not found | `ResourceNotFoundException` | 404 |
| You can only access your own files. | `AccessDeniedException` | 403 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
