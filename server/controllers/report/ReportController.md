# ReportController

Base path `/api/reports`. Source: `controllers/report/ReportController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `POST /api/reports` | `ReportService.generate` | Generates the report, stores it as the caller's media, and returns where to download it. | any signed-in user | body `ReportRequest` | `MediaResponse` |
