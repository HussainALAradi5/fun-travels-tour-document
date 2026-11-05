# CountryService

Source: `services/geography/CountryService.java`.

## Functions

### `List<Country> getAllCountries()`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `Country getCountryById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country not found | `ResourceNotFoundException` | 404 |

### `Country createCountry(CountryCreateRequest request)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country code   already exists. | `DuplicateResourceException` | 409 |

### `Country syncFromExternal(String name)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country not found with name: | `ResourceNotFoundException` | 404 |
| Country lookup failed for | `ExternalServiceException` | 502 |
| REST_COUNTRIES_API_KEY is not configured | `ExternalServiceException` | 502 |
| Rest Countries returned an empty response | `ExternalServiceException` | 502 |
| Rest Countries returned an error response: | `ExternalServiceException` | 502 |

### `Map<String, Integer> syncAllCountries()`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country sync failed | `ExternalServiceException` | 502 |
| REST_COUNTRIES_API_KEY is not configured | `ExternalServiceException` | 502 |
| Rest Countries returned an empty response | `ExternalServiceException` | 502 |
| Rest Countries returned an error response: | `ExternalServiceException` | 502 |

### `void deleteCountry(Integer id)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country not found | `ResourceNotFoundException` | 404 |
