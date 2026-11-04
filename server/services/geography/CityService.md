# CityService

Source: `services/geography/CityService.java`.

## Functions

### `List<City> getAllCities()`

**Runs in:** read-only transaction

### `List<City> getCitiesByCountry(Integer countryId)`

**Runs in:** read-only transaction

### `City createCity(CityCreateRequest request)`

**Runs in:** transaction

### `void deleteCity(Integer id)`

**Runs in:** transaction
