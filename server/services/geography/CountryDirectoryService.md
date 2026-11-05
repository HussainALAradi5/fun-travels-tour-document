# CountryDirectoryService

Source: `services/geography/CountryDirectoryService.java`.

Loads every country (names, ISO code, dial code, flags) from a free public dataset that needs no API key: the `world-countries` package on jsDelivr (`app.countries.directory-url`). Existing countries keep the values they have; only empty fields are filled.

## Functions

### `Map<String, Integer> importAll()`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country directory returned no records | `ExternalServiceException` | 502 |
| Country directory could not be loaded | `ExternalServiceException` | 502 |

### `long countryCount()`

**Exceptions:** none of its own; failures come from the functions it calls.
