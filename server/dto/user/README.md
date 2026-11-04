# user DTOs

Source: `dto/user/`. Clients mirror these in `src/dtos/user/`.

## EmployeeCreateRequest

request record. Staff account created by an administrator, agency owner, or branch manager.

| Field | Type | Rules |
| --- | --- | --- |
| `userName` | `String` | required, not blank |
| `name` | `String` | required, not blank |
| `email` | `String` | required, not blank; Email must be valid |
| `password` | `String` | required, not blank; Password must be at least 6 characters |
| `mobileNumber` | `String` | required, not blank; + country code and number, e.g. +97339990001 (E.164) |
| `age` | `Integer` | Age cannot be negative; Age must be realistic |
| `userType` | `UserTypeEnum` | required |

## ProfileResponse

response record; built by `from(User)`. Everything the profile page shows in one response: identity, contact, role, agency placement, wallet, and membership date.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `code` | `String` | - |
| `userName` | `String` | - |
| `name` | `String` | - |
| `email` | `String` | - |
| `mobileNumber` | `String` | - |
| `age` | `Integer` | - |
| `userType` | `UserTypeEnum` | - |
| `profileImageUrl` | `String` | - |
| `active` | `boolean` | - |
| `agency` | `AgencySummary` | - |
| `agencyBranch` | `BranchSummary` | - |
| `wallet` | `AccountResponse` | - |
| `memberSince` | `LocalDateTime` | - |

## UserContactSummary

response record; built by `from(User)`. A user with their email, for records where contacting them is the point (agency owner).

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `name` | `String` | - |
| `email` | `String` | - |

## UserResponse

response record; built by `from(User)`. A user account as lists and sign-in return it.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `userName` | `String` | - |
| `name` | `String` | - |
| `email` | `String` | - |
| `mobileNumber` | `String` | - |
| `age` | `Integer` | - |
| `userType` | `UserTypeEnum` | - |
| `profileImageUrl` | `String` | - |
| `active` | `boolean` | - |
| `agency` | `AgencySummary` | - |
| `agencyBranch` | `BranchSummary` | - |

## UserSummary

response record; built by `from(User)`. A user as other records show them: id and display name.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `name` | `String` | - |

## UserUpdateRequest

request record. Self-service profile fields. Role, agency, email, and password are changed elsewhere.

| Field | Type | Rules |
| --- | --- | --- |
| `name` | `String` | - |
| `mobileNumber` | `String` | + country code and number, e.g. +97339990001 (E.164) |
| `age` | `Integer` | Age cannot be negative; Age must be realistic |
| `base64Image` | `String` | - |
| `removeImage` | `boolean` | - |
