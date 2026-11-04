# agency DTOs

Source: `dto/agency/`. Clients mirror these in `src/dtos/agency/`.

## AgencyBranchCreateRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `branchName` | `String` | required, not blank |
| `branchAddress` | `String` | - |
| `contactNumber` | `String` | - |
| `branchManagerId` | `Integer` | - |

## AgencyBranchResponse

response record; built by `from(AgencyBranch)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `branchName` | `String` | - |
| `branchAddress` | `String` | - |
| `contactNumber` | `String` | - |
| `agency` | `AgencySummary` | - |
| `branchManager` | `UserSummary` | - |
| `active` | `boolean` | - |

## AgencyCreateRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `agencyName` | `String` | required, not blank |
| `address` | `String` | - |
| `contactNumber` | `String` | - |
| `ownerMobileNumber` | `String` | - |
| `countryId` | `Integer` | - |
| `cityId` | `Integer` | - |
| `agencyOwnerId` | `Integer` | - |

## AgencyResponse

response record; built by `from(Agency)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `agencyName` | `String` | - |
| `address` | `String` | - |
| `contactNumber` | `String` | - |
| `ownerMobileNumber` | `String` | - |
| `country` | `CountrySummary` | - |
| `city` | `CitySummary` | - |
| `agencyOwner` | `UserContactSummary` | - |
| `active` | `boolean` | - |

## AgencySummary

response record; built by `from(Agency)`. An agency by id and name.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `agencyName` | `String` | - |

## BranchSummary

response record; built by `from(AgencyBranch)`. An agency branch by id and name.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `branchName` | `String` | - |
