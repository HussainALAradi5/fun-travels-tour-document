# ReportController

Base path `/api/v1/reports`. Source: `controllers/report/ReportController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `POST /api/v1/reports` | `ReportService.generate` | Generates the report, stores it as the caller's media, and returns where to download it. | any signed-in user | body `ReportRequest` | `MediaResponse` | 400, 401, 403 |
