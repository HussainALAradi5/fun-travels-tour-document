# ReportService

Source: `services/report/ReportService.java`.

Generates a branded PDF or Excel report and keeps it as the requester's media.

## Business logic

`generate` checks the caller's role against the `ReportType` (customers: tour catalog, their tickets, their ledger; staff: tours, passenger manifest, fleet, meals, agency branches and employees; admins and managers: user directory), loads the rows through `ReportDataService`, renders the branded PDF (OpenPDF) or Excel (Apache POI) file, and stores it with `MediaService` as the caller's REPORT media. Rendering happens outside the database transaction.

## Functions

### `Media generate(ReportRequest request)`
