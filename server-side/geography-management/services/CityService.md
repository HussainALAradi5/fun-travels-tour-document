# City Service

**Source:** `src/main/java/com/server/server/services/CityService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions |
|---|---|---|---|---|---|
| `public List<City> getAllCities()` | None | Calls `findAll`. | Supplies geography selectors. | All cities; read-only. | None directly. |
| `public List<City> getCitiesByCountry(Integer countryId)` | Required country ID | Queries by parent country. | City selection must be country-scoped. | Matching cities; read-only. | Null: `"countryId must not be null"`. |
| `public City createCity(City city)` | City with country ID | Validates country reference, checks case-insensitive uniqueness within country, saves. | Prevents orphan and duplicate city records. | Created city. | `"Valid Country is required to add a city."`; `"City '{name}' already exists in this country."` |
| `public void deleteCity(Integer id)` | Required city ID | Verifies existence then deletes. | Produces a clear missing-resource failure. | Deletes city. | `ResourceNotFoundException("City", id)`. |

## Expected behavior and displayed errors

### `getAllCities()`

Returns all configured cities for administration and selector data. It is read-only. Unexpected repository failures must be returned as a generic safe request error without SQL or Hibernate details.

### `getCitiesByCountry(Integer countryId)`

Returns only cities whose parent is the requested country. This prevents a user from selecting an invalid country/city combination. A null ID displays `countryId must not be null`.

### `createCity(City city)`

The function must resolve a valid parent country, check case-insensitive uniqueness inside that country, then save and return the city. A missing/invalid parent displays `Valid Country is required to add a city.` A duplicate displays `City '{name}' already exists in this country.` No partial record should remain after failure.

### `deleteCity(Integer id)`

The function verifies the city exists before deletion. A missing record displays the standard `City` resource-not-found message with its ID. A referential-integrity conflict should be translated to a clear message such as `This city cannot be deleted because it is currently in use.`
