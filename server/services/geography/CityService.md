# CityService

Source: `services/geography/CityService.java`.

## Functions

### `List<City> getAllCities()`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `List<City> getCitiesByCountry(Integer countryId)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `City createCity(CityCreateRequest request)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Country not found | `ResourceNotFoundException` | 404 |
| City ' ' already exists in this country. | `DuplicateResourceException` | 409 |

### `void deleteCity(Integer id)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| City not found | `ResourceNotFoundException` | 404 |
