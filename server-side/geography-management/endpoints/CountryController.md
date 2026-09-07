# CountryController

**File:** `src/main/java/com/server/server/controllers/CountryControllers.java`
**Base Path:** `/api/countries`

## Endpoints

### GET /api/countries

**Description:** Get all countries
**Service Method:** `CountryService.getAllCountries()`
**Response (200 OK):** List of Country entities
**Access:** Public

---

### POST /api/countries/sync/{name}

**Description:** Sync a country from RestCountries API
**Service Method:** `CountryService.syncFromExternal(name, userType)`
**Path Params:** name (String) - Country name
**Query Params:** userType (String) - Must be "ADMIN"
**Response (200 OK):** Synced Country entity
**Access:** ADMIN

---

### POST /api/countries

**Description:** Create country manually
**Service Method:** `CountryService.createCountry(country, userType)`
**Request Body:** Country entity
**Query Params:** userType (String) - Must be "ADMIN"
**Response (200 OK):** Created Country entity
**Access:** ADMIN

---

### POST /api/countries/sync-all

**Description:** Sync all countries from external API
**Service Method:** `CountryService.syncAllCountries(userType)`
**Query Params:** userType (String) - Must be "ADMIN"
**Response (200 OK):** { added, skipped }
**Access:** ADMIN

---

### DELETE /api/countries/{id}

**Description:** Delete a country
**Service Method:** `CountryService.deleteCountry(id, userType)`
**Path Params:** id (Integer) - Country ID
**Query Params:** userType (String) - Must be "ADMIN"
**Access:** ADMIN
