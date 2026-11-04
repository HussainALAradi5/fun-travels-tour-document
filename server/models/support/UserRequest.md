# UserRequest

Table `user_requests`. Inherits `BaseEntity`. Source: `models/support/UserRequest.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `title` | `String` |  required |
| `description` | `String` |  required |
| `type` | `UserRequestType` |  required |
| `status` | `UserRequestStatus` |   |
| `user` | `User` | ManyToOne required |
| `assignedTo` | `User` | ManyToOne  |
| `solvedBy` | `User` | ManyToOne  |
| `solvedAt` | `LocalDateTime` |   |
