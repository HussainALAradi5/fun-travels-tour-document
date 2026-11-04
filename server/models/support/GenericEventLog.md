# GenericEventLog

Table `generic_event_logs`. Inherits `BaseEntity`. Source: `models/support/GenericEventLog.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `referenceId` | `Integer` |  required |
| `referenceType` | `ReferenceType` |  required |
| `action` | `String` |  required |
| `description` | `String` |   |
| `actor` | `User` | ManyToOne required |
