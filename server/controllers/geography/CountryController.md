# CountryController

Base path `/api/countries`. Source: `controllers/geography/CountryController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/countries` | `CountryService.getAllCountries` | Get all. | public | - | `List<CountryResponse>` | - |
| `POST /api/countries/sync/{name}` | `CountryService.syncFromExternal` | Sync external. | ADMIN | - | `CountryResponse` | 401, 403, 404, 502 |
| `POST /api/countries` | `CountryService.createCountry` | Add manual. | ADMIN | body `CountryCreateRequest` | `CountryResponse` | 400, 401, 403, 409 |
| `POST /api/countries/sync-all` | `CountryService.syncAllCountries` | Every country: from REST Countries v5 when a key is configured, otherwise from the free country directory. | ADMIN | - | `Map<String, Integer>` | 401, 403, 502 |
| `DELETE /api/countries/{id}` | `CountryService.deleteCountry` | Delete country. | ADMIN | - | `Void` | 401, 403, 404 |
