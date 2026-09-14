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
