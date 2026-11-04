# AgencyService

Source: `services/agency/AgencyService.java`.

## Business logic

- `getAllAgencies` and `searchAgencies`: administrators see every agency; agency staff only their own; other roles are refused for search.
- `getVisibleAgency` (the `GET /api/agencies/{id}` endpoint) and `getEmployeesByAgencyId`: administrators and the agency's own staff only, because the response holds the owner's and staff members' contacts.
- `createAgency` (admin): city must belong to the country, names are unique per country, and the optional owner must have the OWNER role.

## Functions

### `List<Agency> getAllAgencies()`

**Purpose:** Admins see every agency; agency staff only their own.

**Runs in:** read-only transaction

### `PageResponse<Agency> searchAgencies(String query, Integer page, Integer size)`

**Purpose:** Admins search every agency; agency staff find only their own; other roles are refused.

**Runs in:** read-only transaction

### `Agency getVisibleAgency(Integer id)`

**Purpose:** Agency details (owner contacts included) for administrators and the agency's own staff.

**Runs in:** read-only transaction

### `Agency getAgencyById(Integer id)`

**Runs in:** read-only transaction

### `Agency createAgency(AgencyCreateRequest request)`

**Purpose:** Admin-only. The optional owner must already have the OWNER role.

**Runs in:** transaction

### `List<User> getEmployeesByAgencyId(Integer agencyId)`

**Runs in:** read-only transaction
