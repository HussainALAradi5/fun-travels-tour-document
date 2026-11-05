# TourService

Source: `services/tourmanagement/TourService.java`.

Creating and editing tours, with their validation rules.

## Business logic

### `create(TourCreateRequest request)`

Agency staff create tours for their own agency (and branch, when they have one). Cities must belong to their countries, start date cannot be in the past, capacity cannot exceed the vehicle capacity, the vehicle cannot serve an overlapping tour, and offered meals must be ACTIVE and belong to the tour's agency (or be shared). New tours start PENDING. The price is `basePrice` minus `discountPrice` (`totalPrice`).

### `updateTour(Integer id, TourUpdateRequest request)`

Who may manage a tour (`requireCanManage`, also used by the status workflow): admins always; owners for their agency; managers for their branch or branch-less tours of their agency; employees only tours they created. Capacity cannot drop below sold/held places. The vehicle cannot change once tickets exist (`TRANSPORTATION_LOCKED`).

Reading tours is in `TourCatalogService`, the status workflow in `TourStatusService`, and nightly housekeeping in `TourSchedulerService`.

## Functions

### `Tour getById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Tour not found | `ResourceNotFoundException` | 404 |

### `Tour create(TourCreateRequest request)`

**Runs in:** transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Start country not found. | `WorkflowException` | 409 |
| End country not found. | `WorkflowException` | 409 |
| Start city not found. | `WorkflowException` | 409 |
| End city not found. | `WorkflowException` | 409 |
| A selected city must belong to its selected country. | `WorkflowException` | 409 |
| Transportation is already assigned to an overlapping tour. | `WorkflowException` | 409 |
| Start date is required. | `WorkflowException` | 409 |
| Start date cannot be in the past. | `WorkflowException` | 409 |
| End date cannot be earlier than the start date. | `WorkflowException` | 409 |
| Tour capacity must be greater than zero. | `WorkflowException` | 409 |
| Tour capacity cannot exceed transportation capacity. | `WorkflowException` | 409 |
| Discount cannot exceed the base price. | `WorkflowException` | 409 |
| One or more meal plans were not found. | `ResourceNotFoundException` | 404 |
| Meal ' ' is not active. | `WorkflowException` `MEAL_INACTIVE` | 409 |
| Meal ' ' belongs to another agency. | `WorkflowException` `MEAL_OTHER_AGENCY` | 409 |

### `Tour updateTour(Integer id, TourUpdateRequest request)`

**Runs in:** transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Cannot modify a completed tour. | `WorkflowException` | 409 |
| Capacity cannot be lower than the number of reserved or sold places. | `WorkflowException` `CAPACITY_BELOW_BOOKINGS` | 409 |
| A selected city must belong to its selected country. | `WorkflowException` | 409 |
| Transportation cannot change after tickets were issued for this tour. | `WorkflowException` `TRANSPORTATION_LOCKED` | 409 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Transportation is already assigned to an overlapping tour. | `WorkflowException` | 409 |
| Start date is required. | `WorkflowException` | 409 |
| Start date cannot be in the past. | `WorkflowException` | 409 |
| End date cannot be earlier than the start date. | `WorkflowException` | 409 |
| Tour capacity must be greater than zero. | `WorkflowException` | 409 |
| Tour capacity cannot exceed transportation capacity. | `WorkflowException` | 409 |
| Discount cannot exceed the base price. | `WorkflowException` | 409 |
| Tour not found | `ResourceNotFoundException` | 404 |
| Country not found | `ResourceNotFoundException` | 404 |
| City not found | `ResourceNotFoundException` | 404 |
| One or more meal plans were not found. | `ResourceNotFoundException` | 404 |
| Meal ' ' is not active. | `WorkflowException` `MEAL_INACTIVE` | 409 |
| Meal ' ' belongs to another agency. | `WorkflowException` `MEAL_OTHER_AGENCY` | 409 |
