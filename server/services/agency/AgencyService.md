# AgencyService

Source: `services/agency/AgencyService.java`.

## Functions

### `List<Agency> getAllAgencies()`

**Runs in:** read-only transaction

### `PageResponse<Agency> searchAgencies(String query, Integer page, Integer size)`

**Runs in:** read-only transaction

### `Agency getAgencyById(Integer id)`

**Runs in:** read-only transaction

### `Agency createAgency(AgencyCreateRequest request)`

**Purpose:** Admin-only. The optional owner must already have the OWNER role.

**Runs in:** transaction

### `List<User> getEmployeesByAgencyId(Integer agencyId)`

**Runs in:** read-only transaction
