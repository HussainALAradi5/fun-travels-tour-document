# CountryService

**File:** `src/main/java/com/server/server/services/CountryService.java`

## Methods

### getAllCountries() -> List<Country>

**Parameters:** None
**Returns:** List of all countries

---

### syncFromExternal(name, userType) -> Country

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| name | String | Country name to sync |
| userType | String | Must be "ADMIN" |

**Returns:** Synced Country entity

**Business Logic:**
1. Validates admin access
2. Fetches country data from RestCountries API
3. Creates or updates country record
4. Downloads flag images

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Access Denied" |
| RuntimeException | "Country not found in external API" |

---

### createCountry(Country, userType) -> Country

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| country | Country | Country entity |
| userType | String | Must be "ADMIN" |

**Returns:** Created Country entity

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Access Denied" |

---

### syncAllCountries(userType) -> Map<String, Integer>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| userType | String | Must be "ADMIN" |

**Returns:** Map with "added" and "skipped" counts

---

### deleteCountry(id, userType) -> void

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Country ID |
| userType | String | Must be "ADMIN" |

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Access Denied" |
| RuntimeException | Country not found |
