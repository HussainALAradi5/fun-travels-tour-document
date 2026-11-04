# CountryService

Source: `services/geography/CountryService.java`.

## Functions

### `List<Country> getAllCountries()`

**Runs in:** read-only transaction

### `Country getCountryById(Integer id)`

**Runs in:** read-only transaction

### `Country createCountry(CountryCreateRequest request)`

**Runs in:** transaction

### `Country syncFromExternal(String name)`

**Runs in:** transaction

### `Map<String, Integer> syncAllCountries()`

**Runs in:** transaction

### `void deleteCountry(Integer id)`

**Runs in:** transaction
