# GenericComment

Table `generic_comments`. Inherits `BaseEntity`. Source: `models/support/GenericComment.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `referenceId` | `Integer` |  required |
| `referenceType` | `ReferenceType` |  required |
| `content` | `String` |  required |
| `author` | `User` | ManyToOne required |
