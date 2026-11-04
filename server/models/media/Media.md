# Media

Table `media`. Inherits `BaseEntity`. Source: `models/media/Media.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `fileName` | `String` |  required |
| `contentType` | `String` |  required |
| `sizeBytes` | `long` |  required |
| `storagePath` | `String` |  unique, required |
| `category` | `MediaCategory` |  required |
| `owner` | `User` | ManyToOne required |
| `reportType` | `ReportType` |   |
| `reportFormat` | `ReportFormat` |   |
| `recordCount` | `Integer` |   |
