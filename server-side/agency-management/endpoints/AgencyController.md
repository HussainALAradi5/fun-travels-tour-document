# AgencyController

**File:** `src/main/java/com/server/server/controllers/agency/AgencyController.java`
**Base Path:** `/api/agencies`

## Endpoints

### GET /api/agencies

**Description:** Get all agencies
**Service Method:** `AgencyService.getAllAgencies()`
**Response (200 OK):**
```json
{
  "success": true,
  "message": "Fetched all agencies",
  "data": []
}
```
**Access:** Public

---

### GET /api/agencies/{id}

**Description:** Get agency by ID
**Service Method:** `AgencyService.getAgencyById(id)`
**Path Params:** id (Integer) - Agency ID
**Response (200 OK):** Agency entity
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | "Agency not found with ID: {id}" |
**Access:** Public

---

### POST /api/agencies

**Description:** Create a new agency
**Service Method:** `AgencyService.createAgencyFromMap(payload)`
**Request Body:**
```json
{
  "agencyName": "string",
  "address": "string",
  "contactNumber": "string",
  "countryId": 1,
  "cityId": 1,
  "agencyOwnerId": 1
}
```
**Response (200 OK):** Created Agency entity
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Country/City/Owner not found |
**Access:** ADMIN, OWNER

---

### GET /api/agencies/{id}/employees

**Description:** Get agency employees
**Service Method:** `AgencyService.getEmployeesByAgencyId(id)`
**Path Params:** id (Integer) - Agency ID
**Response (200 OK):** List of User entities
**Access:** ADMIN, OWNER, MANAGER
