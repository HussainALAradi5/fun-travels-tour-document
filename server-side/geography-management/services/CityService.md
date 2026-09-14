# City Service

**Source:** `src/main/java/com/server/server/services/CityService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions |
|---|---|---|---|---|---|
| `public List<City> getAllCities()` | None | Calls `findAll`. | Supplies geography selectors. | All cities; read-only. | None directly. |
| `public List<City> getCitiesByCountry(Integer countryId)` | Required country ID | Queries by parent country. | City selection must be country-scoped. | Matching cities; read-only. | Null: `"countryId must not be null"`. |
| `public City createCity(City city)` | City with country ID | Validates country reference, checks case-insensitive uniqueness within country, saves. | Prevents orphan and duplicate city records. | Created city. | `"Valid Country is required to add a city."`; `"City '{name}' already exists in this country."` |
| `public void deleteCity(Integer id)` | Required city ID | Verifies existence then deletes. | Produces a clear missing-resource failure. | Deletes city. | `ResourceNotFoundException("City", id)`. |
