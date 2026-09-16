# Geography Management Endpoints

This table is the feature-owned HTTP contract. Business rules and exception details are documented in this folder's service pages.

| ID | Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|---|
| EP-1 | `GET` | `/api/countries` | Populate country selection. | None | `CountryService` | `getAllCountries` |
| EP-2 | `POST` | `/api/countries` | Add a country manually. | `Country` body | `CountryService` | `createCountry` |
| EP-3 | `POST` | `/api/countries/sync/{name}` | Import one country from the external provider. | Country name | `CountryService` | `syncFromExternal` |
| EP-4 | `POST` | `/api/countries/sync-all` | Synchronize the country catalog. | None | `CountryService` | `syncAllCountries` |
| EP-5 | `DELETE` | `/api/countries/{id}` | Remove a country. | Country ID | `CountryService` | `deleteCountry` |
| EP-6 | `GET` | `/api/cities` | Populate city selection. | None | `CityService` | `getAllCities` |
| EP-7 | `GET` | `/api/cities/country/{countryId}` | Return cities within a country. | Country ID | `CityService` | `getCitiesByCountry` |
| EP-8 | `POST` | `/api/cities` | Add a city. | `City` body | `CityService` | `createCity` |
| EP-9 | `DELETE` | `/api/cities/{id}` | Remove a city. | City ID | `CityService` | `deleteCity` |
| EP-10 | `GET` | `/api/ports` | List active transport ports. | None | `PortService` | `getAllActivePorts` |
| EP-11 | `POST` | `/api/ports` | Create a transport port. | Validated `Port` | `PortService` | `createPort` |
| EP-12 | `PUT` | `/api/ports/{id}/status` | Change port lifecycle status. | Port ID and status | `PortService` | `updateStatus` |

## Endpoint rules

- Authentication and role authorization are enforced by the server.
- Request validation occurs before business-state changes.
- Success and error responses use the shared API envelope.
- Collection endpoints use bounded pagination where supported.

