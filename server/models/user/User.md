# User

Table `users`. Inherits `BaseEntity`. Source: `models/user/User.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `userName` | `String` |  required |
| `name` | `String` |   |
| `email` | `String` |  unique, required |
| `password` | `String` |  required |
| `age` | `int` |   |
| `userType` | `UserTypeEnum` |   |
| `mobileNumber` | `String` |  unique, required |
| `agency` | `Agency` | ManyToOne  |
| `agencyBranch` | `AgencyBranch` | ManyToOne  |
| `isActive` | `boolean` |   |
| `profileImageUrl` | `String` |   |
| `base64Image` | `String` |  not stored |
| `resetToken` | `String` |   |
| `resetTokenExpiry` | `java.time.LocalDateTime` |   |
| `account` | `Account` | OneToOne  |
