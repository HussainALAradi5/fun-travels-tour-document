# CountryControllers

Base path `/api/countries`. Source: `controllers/geography/CountryControllers.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/countries` | `CountryService.getAllCountries` | Get all. | public | - | `List<CountryResponse>` |
| `POST /api/countries/sync/{name}` | `CountryService.syncFromExternal` | Sync external. | ADMIN | - | `CountryResponse` |
| `POST /api/countries` | `CountryService.createCountry` | Add manual. | ADMIN | body `Country` | `CountryResponse` |
| `POST /api/countries/sync-all` | `CountryService.syncAllCountries` | Sync all. | ADMIN | - | `Map<String, Integer>` |
| `DELETE /api/countries/{id}` | `CountryService.deleteCountry` | Delete country. | ADMIN | - | `Void` |
