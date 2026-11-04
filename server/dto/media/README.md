# media DTOs

Source: `dto/media/`. Clients mirror these in `src/dtos/media/`.

## MediaFile

response record. A stored file's bytes with the name and type to send it under.

| Field | Type | Rules |
| --- | --- | --- |
| `fileName` | `String` | - |
| `contentType` | `String` | - |
| `content` | `byte[]` | - |

## MediaResponse

response record; built by `from(Media)`. A stored file as clients see it; the storage path stays on the server.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `code` | `String` | - |
| `fileName` | `String` | - |
| `contentType` | `String` | - |
| `sizeBytes` | `long` | - |
| `category` | `MediaCategory` | - |
| `reportType` | `ReportType` | - |
| `reportFormat` | `ReportFormat` | - |
| `recordCount` | `Integer` | - |
| `createdAt` | `LocalDateTime` | - |
| `downloadPath` | `String` | - |
