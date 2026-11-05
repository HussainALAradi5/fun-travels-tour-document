# ReportDataService

Source: `services/report/ReportDataService.java`.

Loads a report's rows through the domain services, so every scoping rule (own records for customers, own agency for staff) applies exactly as on the list pages. Runs in one read-only transaction and returns plain values, so rendering needs no database access.

## Business logic

Loads report rows through the same service methods the list pages use, so every scoping rule applies unchanged: customers see their own tickets and transactions, agency staff their own agency's tours, vehicles, meals, tickets, and staff. Paged sources are read page by page (100 per page) up to `ReportRules.MAX_ROWS` (5000); larger reports are cut and say so. The passenger manifest needs `tourId` and access to the tour's agency; agency branches and employees need `agencyId` and access to that agency. Runs in one read-only transaction and returns plain values (`ReportTable`).

## Functions

### `ReportTable load(ReportRequest request, User actor)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| This report needs  . | `WorkflowException` `REPORT_PARAMETER_REQUIRED` | 409 |
