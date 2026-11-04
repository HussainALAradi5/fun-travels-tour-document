# Agency

Table `agencies`. Inherits `BaseEntity`. Source: `models/agency/Agency.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `agencyName` | `String` |  required |
| `address` | `String` |   |
| `contactNumber` | `String` |   |
| `agencyOwner` | `User` | ManyToOne  |
| `userType` | `UserTypeEnum` |   |
| `ownerMobileNumber` | `String` |   |
| `country` | `Country` | ManyToOne  |
| `city` | `City` | ManyToOne  |
| `branches` | `List<AgencyBranch>` | OneToMany  |
| `isActive` | `boolean` |   |
| `employees` | `List<User>` | OneToMany  |
