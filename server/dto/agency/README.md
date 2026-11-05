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

## AgencyPolicyResponse

response record; built by `from(Agency)`. An agency's discount and cancellation rules as customers see them before booking.

| Field | Type | Rules |
| --- | --- | --- |
| `agencyId` | `Integer` | - |
| `kidsDiscountPercent` | `int` | - |
| `fullRefundDays` | `int` | - |
| `partialRefundDays` | `int` | - |
| `partialRefundPercent` | `int` | - |
| `summary` | `String` | - |

## AgencyPolicyUpdateRequest

request record. New discount and cancellation rules for an agency; the partial-refund window must start no later than the full one.

| Field | Type | Rules |
| --- | --- | --- |
| `kidsDiscountPercent` | `Integer` | required; Kids discount cannot be negative; Kids discount cannot exceed 100% |
| `fullRefundDays` | `Integer` | required; Days cannot be negative; Use at most 365 days |
| `partialRefundDays` | `Integer` | required; Days cannot be negative; Use at most 365 days |
| `partialRefundPercent` | `Integer` | required; Refund cannot be negative; Refund cannot exceed 100% |

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
