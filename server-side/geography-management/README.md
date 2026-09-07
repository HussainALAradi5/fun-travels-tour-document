# Geography Management

Manages countries, cities, and transportation ports.

## Entities
- **Country** - Country with flag images and codes
- **City** - City belonging to a country
- **Port** - Transportation hub (airport, seaport, etc.)

## Services
- [CountryService](services/CountryService.md) - Country CRUD and external API sync
- [CityService](services/CityService.md) - City management
- [PortService](services/PortService.md) - Port management

## Endpoints
- [CountryController](endpoints/CountryController.md) - `/api/countries`
- [CityController](endpoints/CityController.md) - `/api/cities`
- [PortController](endpoints/PortController.md) - `/api/ports`

## Business Logic
- Countries can be synced from RestCountries external API
- Cities are linked to countries
- Ports have types (AIRPORT, SEAPORT, TRAIN_STATION, etc.)
