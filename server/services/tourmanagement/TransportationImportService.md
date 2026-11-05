# TransportationImportService

Source: `services/tourmanagement/TransportationImportService.java`.

Bulk vehicle registration from a spreadsheet; each row goes through the normal create rules.

## Business logic

`importExcel` reads one vehicle per row (registration, code, type, provider, capacity, agency, optional branch, and counts of premium, accessible, and kids seats) and registers each through `TransportationService.create`, so every create rule and agency limit applies. Row errors are collected and returned in `ImportResult`; valid rows are still imported.

## Functions

### `ImportResult importExcel(InputStream input)`
