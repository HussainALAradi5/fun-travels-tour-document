# geography DTOs

Source: `dto/geography/`. Clients mirror these in `src/dtos/geography/`.

## CityCreateRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `name` | `String` | required, not blank |
| `country` | `EntityReference` | required; nested values validated |

## CityResponse

response record; built by `from(City)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `name` | `String` | - |
| `country` | `CountrySummary` | - |

## CitySummary

response record; built by `from(City)`. A city by id and name.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `name` | `String` | - |

## CountryCreateRequest

request record. Manual country entry; `countryCode` is ISO 3166-1 alpha-2.

| Field | Type | Rules |
| --- | --- | --- |
| `famousName` | `String` | required, not blank |
| `officialName` | `String` | - |
| `countryCode` | `String` | required, not blank; Country code must be two letters (ISO 3166-1 alpha-2) |
| `dialCode` | `String` | Dial code must look like +973 |
| `mobileNumberLength` | `Integer` | Mobile number length must be positive |
| `flagPngUrl` | `String` | - |
| `flagSvgUrl` | `String` | - |

## CountryResponse

response record; built by `from(Country)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `famousName` | `String` | - |
| `officialName` | `String` | - |
| `countryCode` | `String` | - |
| `flagPngUrl` | `String` | - |
| `flagSvgUrl` | `String` | - |
| `dialCode` | `String` | - |
| `mobileNumberLength` | `Integer` | - |

## CountrySummary

response record; built by `from(Country)`. A country with the names and flag that lists and cards display.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `famousName` | `String` | - |
| `officialName` | `String` | - |
| `flagPngUrl` | `String` | - |

## PortCreateRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `portName` | `String` | required, not blank |
| `portCode` | `String` | - |
| `portType` | `PortType` | required |
| `city` | `EntityReference` | required; nested values validated |
| `country` | `EntityReference` | required; nested values validated |
| `latitude` | `Double` | Latitude must be between -90 and 90 |
| `longitude` | `Double` | Longitude must be between -180 and 180 |

## PortResponse

response record; built by `from(Port)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `portName` | `String` | - |
| `portCode` | `String` | - |
| `portType` | `PortType` | - |
| `city` | `CitySummary` | - |
| `country` | `CountrySummary` | - |
| `latitude` | `Double` | - |
| `longitude` | `Double` | - |
| `status` | `GenericStatus` | - |
