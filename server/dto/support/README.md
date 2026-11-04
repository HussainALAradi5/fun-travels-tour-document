# support DTOs

Source: `dto/support/`. Clients mirror these in `src/dtos/support/`.

## CommentRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `content` | `String` | required, not blank |

## CommentResponse

response record; built by `from(GenericComment)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `referenceType` | `ReferenceType` | - |
| `referenceId` | `Integer` | - |
| `content` | `String` | - |
| `author` | `UserSummary` | - |
| `createdAt` | `LocalDateTime` | - |
| `updatedAt` | `LocalDateTime` | - |

## EventLogResponse

response record; built by `from(GenericEventLog)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `referenceType` | `ReferenceType` | - |
| `referenceId` | `Integer` | - |
| `action` | `String` | - |
| `description` | `String` | - |
| `actor` | `UserSummary` | - |
| `createdAt` | `LocalDateTime` | - |

## TimelineResponse

response record.

| Field | Type | Rules |
| --- | --- | --- |
| `events` | `List<EventLogResponse>` | - |
| `comments` | `List<CommentResponse>` | - |

## UserRequestCreateRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `title` | `String` | required, not blank |
| `description` | `String` | required, not blank |
| `type` | `UserRequestType` | required |

## UserRequestFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| (inherited) | `GenericFilterRequest` | `page`, `size`, `search`, `sortBy`, `sortDir` |
| `currentUserId` | `Integer` | optional |
| `status` | `UserRequestStatus` | optional |
| `type` | `UserRequestType` | optional |
| `userIdFilter` | `Integer` | optional |

## UserRequestResponse

response record; built by `from(UserRequest)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `title` | `String` | - |
| `description` | `String` | - |
| `type` | `UserRequestType` | - |
| `status` | `UserRequestStatus` | - |
| `user` | `UserSummary` | - |
| `assignedTo` | `UserSummary` | - |
| `solvedBy` | `UserSummary` | - |
| `solvedAt` | `LocalDateTime` | - |
| `createdAt` | `LocalDateTime` | - |
| `updatedAt` | `LocalDateTime` | - |
