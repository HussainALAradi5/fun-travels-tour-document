# report DTOs

Source: `dto/report/`. Clients mirror these in `src/dtos/report/`.

## ReportRequest

request record. What to export. `tourId` is required for the passenger manifest, `agencyId` for agency branches and employees; `role` narrows the users report.

| Field | Type | Rules |
| --- | --- | --- |
| `type` | `ReportType` | required |
| `format` | `ReportFormat` | required |
| `tourId` | `Integer` | tourId must be positive |
| `agencyId` | `Integer` | agencyId must be positive |
| `role` | `UserTypeEnum` | - |
