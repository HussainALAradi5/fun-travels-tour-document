# AgencyService

**File:** `src/main/java/com/server/server/services/agency/AgencyService.java`

## Methods

### getAllAgencies() -> List<Agency>

**Parameters:** None
**Returns:** List of all agencies
**Business Logic:** Direct repository findAll() call
**Exceptions:** None

---

### getAgencyById(id) -> Agency

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Agency ID |

**Returns:** Agency entity
**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Agency not found with ID: {id}" |

---

### createAgencyFromMap(Map<String, Object>) -> Agency

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| payload | Map<String, Object> | Map with agencyName, address, contactNumber, countryId, cityId, agencyOwnerId |

**Returns:** Created Agency entity

**Business Logic:**
1. Converts payload map to Agency entity via ObjectMapper
2. Resolves Country relationship by countryId
3. Resolves City relationship by cityId
4. Saves and flushes agency (forces DB to generate ID)
5. Links agency owner by agencyOwnerId
6. Updates owner's agency reference
7. Returns complete agency with owner

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Country not found with ID: {id}" |
| RuntimeException | "City not found with ID: {id}" |
| RuntimeException | "Owner User not found with ID: {id}" |
| RuntimeException | "Failed to create agency: {message}" |

---

### getEmployeesByAgencyId(agencyId) -> List<User>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| agencyId | Integer | Agency ID |

**Returns:** List of active users in agency
**Exceptions:** None
