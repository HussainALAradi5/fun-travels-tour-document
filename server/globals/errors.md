# Error envelope

Every response uses `ApiResponse`: `success`, `code`, `message`, `data`, `fieldErrors`, `timestamp`, `path`.

| Status | When | Example `code` |
| --- | --- | --- |
| 400 | Bean validation failed (`fieldErrors` filled), bad parameter type, unreadable body, invalid argument | `VALIDATION_FAILED`, `REQUEST_FAILED` |
| 401 | Missing or invalid token on a protected route; wrong password | - |
| 403 | Role not allowed, record owned by someone else or another agency, deactivated account | `REQUEST_FAILED` |
| 404 | Record not found | `REQUEST_FAILED` |
| 409 | Workflow rule, duplicate value, concurrent update | `INSUFFICIENT_BALANCE`, `SEAT_NOT_AVAILABLE`, `RESERVATION_HOLD_EXPIRED`, `ALREADY_CANCELLED`, `DATE_CONFLICT` |
| 500 | Unexpected error; details are logged, never returned | `REQUEST_FAILED` |

Workflow codes are listed per service in [services](../services/README.md).
