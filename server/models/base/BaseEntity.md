# BaseEntity

Table `-`. Inherits `-`. Source: `models/base/BaseEntity.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `id` | `Integer` |   |
| `code` | `String` |  unique |
| `createdAt` | `LocalDateTime` |   |
| `updatedAt` | `LocalDateTime` |   |
| `createdBy` | `User` | ManyToOne  |
| `updatedBy` | `User` | ManyToOne  |
