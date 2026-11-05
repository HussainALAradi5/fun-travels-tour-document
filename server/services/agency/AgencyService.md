# AgencyService

Source: `services/agency/AgencyService.java`.

## Business logic

- `getAllAgencies` and `searchAgencies`: administrators see every agency; agency staff only their own; other roles are refused for search.
- `getVisibleAgency` (the `GET /api/v1/agencies/{id}` endpoint) and `getEmployeesByAgencyId`: administrators and the agency's own staff only, because the response holds the owner's and staff members' contacts.
- `createAgency` (admin): city must belong to the country, names are unique per country, and the optional owner must have the OWNER role.

## Functions

### `List<Agency> getAllAgencies()`

**Purpose:** Admins see every agency; agency staff only their own.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Agency not found | `ResourceNotFoundException` | 404 |

### `PageResponse<Agency> searchAgencies(String query, Integer page, Integer size)`

**Purpose:** Admins search every agency; agency staff find only their own; other roles are refused.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `Agency getPolicyAgency(Integer id)`

**Purpose:** Discount and cancellation rules; public, so customers can read them before booking.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Agency not found | `ResourceNotFoundException` | 404 |

### `Agency updatePolicy(Integer id, AgencyPolicyUpdateRequest request)`

**Purpose:** Owners change their own agency's rules; administrators any agency's. Applies to prices and refunds from now on.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Only the agency owner can change its discount and refund rules. | `AccessDeniedException` | 403 |
| The partial refund window must start no later than the full refund window. | `IllegalArgumentException` | 400 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Agency not found | `ResourceNotFoundException` | 404 |

### `Agency getVisibleAgency(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Agency not found | `ResourceNotFoundException` | 404 |

### `Agency getAgencyById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Agency not found | `ResourceNotFoundException` | 404 |

### `Agency createAgency(AgencyCreateRequest request)`

**Purpose:** Admin-only. The optional owner must already have the OWNER role.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country not found | `ResourceNotFoundException` | 404 |
| City not found | `ResourceNotFoundException` | 404 |
| The selected city does not belong to the selected country. | `IllegalArgumentException` | 400 |
| An agency named ' ' already exists in this country. | `DuplicateResourceException` | 409 |
| User not found | `ResourceNotFoundException` | 404 |
| The selected agency owner must have the OWNER role. | `IllegalArgumentException` | 400 |

### `List<User> getEmployeesByAgencyId(Integer agencyId)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Agency not found | `ResourceNotFoundException` | 404 |
