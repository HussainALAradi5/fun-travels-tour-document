# CityController

Base path `/api/cities`. Source: `controllers/geography/CityController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/cities` | `CityService.getAllCities` | Get all. | public | - | `List<CityResponse>` | - |
| `GET /api/cities/country/{countryId}` | `CityService.getCitiesByCountry` | Get by country. | public | - | `List<CityResponse>` | - |
| `POST /api/cities` | `CityService.createCity` | Create. | ADMIN | body `CityCreateRequest` | `CityResponse` | 400, 401, 403, 404, 409 |
| `DELETE /api/cities/{id}` | `CityService.deleteCity` | Delete. | ADMIN | - | `Void` | 401, 403, 404 |
