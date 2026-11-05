# media DTOs

Source: `dto/media/`. Clients mirror these in `src/dtos/media/`.

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
