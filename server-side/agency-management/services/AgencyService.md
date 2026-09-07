# AgencyService

**File:** `src/main/java/com/server/server/services/Agency/AgencyService.java`

## Methods

### getAllAgencies() -> List<Agency>
Returns all active agencies.

### getAgencyById(id) -> Agency
Returns agency by ID with branches and employees.

### createAgency(Agency) -> Agency
Creates a new agency.

### updateAgency(id, Agency) -> Agency
Updates agency details.

### getVisibleStaff(userId) -> List<User>
Returns staff visible to the requesting user based on their role.

### getEmployeesByAgency(agencyId) -> List<User>
Returns all employees belonging to an agency.
