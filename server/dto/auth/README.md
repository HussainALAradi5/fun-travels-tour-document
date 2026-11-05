# auth DTOs

Source: `dto/auth/`. Clients mirror these in `src/dtos/auth/`.

## AuthResponse

response record.

| Field | Type | Rules |
| --- | --- | --- |
| `token` | `String` | - |
| `user` | `UserResponse` | - |

## LoginRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `identifier` | `String` | required, not blank |
| `password` | `String` | required, not blank |

## PasswordResetConfirmRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `identifier` | `String` | required, not blank |
| `token` | `String` | required, not blank |
| `newPassword` | `String` | required, not blank; Password must be at least 6 characters |

## PasswordResetRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `identifier` | `String` | required, not blank |

## RegisterRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `userName` | `String` | required, not blank; Username must be at most 50 characters |
| `name` | `String` | required, not blank |
| `email` | `String` | required, not blank; Email must be valid |
| `password` | `String` | required, not blank; Password must be at least 6 characters |
| `mobileNumber` | `String` | required, not blank; + country code and number, e.g. +97339990001 (E.164) |
| `age` | `Integer` | Age cannot be negative; Age must be realistic |
| `gender` | `Gender` | required |
