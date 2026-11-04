# AgencyBranch

Table `agency_branch`. Inherits `BaseEntity`. Source: `models/agency/AgencyBranch.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `branchName` | `String` |   |
| `branchAddress` | `String` |   |
| `contactNumber` | `String` |   |
| `ownerMobileNumber` | `String` |   |
| `agency` | `Agency` | ManyToOne  |
| `isActive` | `boolean` |   |
| `country` | `Country` | ManyToOne  |
| `city` | `City` | ManyToOne  |
| `branchManager` | `User` | ManyToOne  |
| `employees` | `List<User>` | OneToMany  |
