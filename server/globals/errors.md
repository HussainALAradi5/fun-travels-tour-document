# Error envelope and codes

Every response uses `ApiResponse` (`utilities/responses/`): `success`, `code`, `message`, `data`, `fieldErrors`, `timestamp`, `path`. Errors from controllers are mapped in `middlewares/errors/GlobalExceptionHandler`; 401, 403 and 429 from the security filters are written by `SecurityErrorResponder` in the same shape. Codes are constants in `constants/errors/ErrorCodes`; clients branch on `code`, not on `message`.

| Status | Code | When | Raised by |
| --- | --- | --- | --- |
| 400 | `VALIDATION_FAILED` | Bean validation failed; `fieldErrors` names each field | `@Valid` request records |
| 400 | `BAD_REQUEST` | Missing or mistyped parameter, unreadable body, or a rule on the input (for example "Only JPEG and PNG images are supported.") | `IllegalArgumentException` |
| 401 | `UNAUTHORIZED` | No or invalid token on a protected route; wrong sign-in details | security filter, `BadCredentialsException` |
| 403 | `FORBIDDEN` | Role not allowed, record owned by someone else or another agency | `AccessDeniedException`, `@PreAuthorize` |
| 403 | `ACCOUNT_DISABLED` | Signing in to a deactivated account | `DisabledException` |
| 404 | `NOT_FOUND` | Record does not exist | `ResourceNotFoundException` |
| 404 | `ROUTE_NOT_FOUND` | Address does not exist (signed-in callers; anonymous callers get 401 first) | Spring MVC |
| 405 | `METHOD_NOT_ALLOWED` | Wrong HTTP method for an address | Spring MVC |
| 409 | workflow code, or `WORKFLOW_CONFLICT` | Business rule: `INSUFFICIENT_BALANCE`, `SEAT_NOT_AVAILABLE`, `RESERVATION_HOLD_EXPIRED`, `ALREADY_CANCELLED`, `DATE_CONFLICT`, `PAYMENT_METHOD_UNSUPPORTED`, ... | `WorkflowException` |
| 409 | `CONFLICT` | State rule such as "only a pending request can be assigned" | `IllegalStateException` |
| 409 | `DUPLICATE_RESOURCE` | Unique value already used | `DuplicateResourceException`, database unique constraint |
| 409 | `CONCURRENT_UPDATE` | Record changed by another request | optimistic locking |
| 413 | `PAYLOAD_TOO_LARGE` | Upload over the size limit | Spring MVC |
| 415 | `UNSUPPORTED_MEDIA_TYPE` | Wrong content type | Spring MVC |
| 429 | `TOO_MANY_REQUESTS` | Too many sign-in, registration or reset attempts; see `Retry-After` | `AuthRateLimitFilter` |
| 500 | `STORAGE_FAILED` | A file could not be written or read | `StorageException` |
| 500 | `DATABASE_ERROR` | Transaction failed for a reason other than validation | `TransactionSystemException` |
| 500 | `INTERNAL_ERROR` | Anything unexpected; details are logged with the request id, never returned | catch-all |
| 502 | `EXTERNAL_SERVICE_FAILED` | The country API is not configured or failed | `ExternalServiceException` |

Each service page lists the cases a function rejects with their exception and status, and each controller table lists the statuses its endpoints can return: see [services](../services/README.md) and [controllers](../controllers/README.md).
