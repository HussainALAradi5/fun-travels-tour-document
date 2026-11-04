# CityController

Base path `/api/cities`. Source: `controllers/geography/CityController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/cities` | `CityService.getAllCities` | Get all. | public | - | `List<CityResponse>` |
| `GET /api/cities/country/{countryId}` | `CityService.getCitiesByCountry` | Get by country. | public | - | `List<CityResponse>` |
| `POST /api/cities` | `CityService.createCity` | Create. | ADMIN | body `CityCreateRequest` | `CityResponse` |
| `DELETE /api/cities/{id}` | `CityService.deleteCity` | Delete. | ADMIN | - | `Void` |
