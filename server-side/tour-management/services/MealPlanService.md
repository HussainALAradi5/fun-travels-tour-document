# Meal Plan Service

**Source:** `src/main/java/com/server/server/services/tourmanagement/MealPlanService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions / authorization |
|---|---|---|---|---|---|
| `public PageResponse<MealPlan> findAll(Integer page, Integer size, String sortDir)` | Pagination | Queries by meal name. | Bounded administration list. | Meal page; read-only. | Pagination errors may propagate. |
| `public MealPlan findById(Integer id)` | Required ID | Queries by ID. | Shared managed-meal resolver. | Meal; read-only. | `"Meal definition not found: {id}"`. |
| `public PageResponse<MealPlan> getAgencyCatalog(Integer agencyId, Integer page, Integer size)` | Agency and pagination | Queries active agency meals ordered by name. | Customers only see active offerings owned by the agency. | Meal page; read-only. | Null agency ID validation. |
| `public MealPlan createMeal(MealPlan meal)` | Meal aggregate | Rejects negative price, forces active, saves. | New offerings start active; prices cannot be negative. | Created meal. | `"Meal price cannot be negative."`; admin/manager/owner. |
| `public MealPlan updateMeal(Integer id, MealPlan incomingData)` | ID and editable fields | Loads, validates price, copies while protecting ID/status/agency, saves. | Updates cannot transfer agency ownership or bypass status workflow. | Updated meal. | Missing meal; negative-price message; admin/manager/owner. |
| `public void updateMealStatus(Integer id, GenericStatus status)` | ID and status | Loads, sets, saves. | Availability changes independently from definition. | Writes status. | Missing meal; admin/manager. |
| `public MealPlan updatePricing(Integer id, Double newPrice)` | ID and nonnegative price | Validates, loads, sets price, saves. | Dedicated pricing command. | Updated meal. | `"Meal price cannot be negative or null."`; admin/manager/owner. |

## Detailed behavior and displayed errors

### `findAll(Integer page, Integer size, String sortDir)`

Returns a bounded meal-plan page ordered by meal name. The call is read-only. Invalid page, size, or sort direction displays the shared pagination validation message.

### `findById(Integer id)`

Returns the managed meal plan. An unknown identifier displays `Meal definition not found: {id}`.

### `getAgencyCatalog(Integer agencyId, Integer page, Integer size)`

Returns active meal plans belonging to the requested agency, ordered by name. Inactive or other-agency offerings must not be shown to customers. A missing agency ID displays the relevant required-parameter validation message.

### `createMeal(MealPlan meal)`

Validates price, forces `ACTIVE`, saves, and returns the created meal. Price must be zero or positive. A negative price displays `Meal price cannot be negative.` Authorization is limited to the documented administration roles.

### `updateMeal(Integer id, MealPlan incomingData)`

Loads the persisted meal, validates the new price, and copies editable fields while protecting ID, lifecycle status, and agency ownership. This prevents a general edit request from moving a meal between agencies or bypassing the status command. Missing meal and negative-price messages are displayed exactly as documented above.

### `updateMealStatus(Integer id, GenericStatus status)`

Changes availability without deleting the meal or its historical references. Missing records display `Meal definition not found: {id}`; invalid status input displays a field-level `status` error.

### `updatePricing(Integer id, Double newPrice)`

Changes only the price and returns the updated meal. Null or negative input displays `Meal price cannot be negative or null.` A failure rolls back the price update.
