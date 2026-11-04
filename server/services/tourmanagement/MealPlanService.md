# MealPlanService

Source: `services/tourmanagement/MealPlanService.java`.

## Business logic

Agency staff create meals for their own agency; admins may name an agency or create a shared meal. Status and price changes are limited to the meal's agency. Inactive meals cannot be added to tours or booked, and tour responses only list active meals.

## Functions

### `PageResponse<MealPlan> findAll(Integer page, Integer size, String sortDir)`

**Runs in:** read-only transaction

### `MealPlan findById(Integer id)`

**Runs in:** read-only transaction

### `PageResponse<MealPlan> getAgencyCatalog(Integer agencyId, Integer page, Integer size)`

**Runs in:** read-only transaction

### `MealPlan createMeal(MealPlanCreateRequest request)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `void updateMealStatus(Integer id, GenericStatus status)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `MealPlan updatePricing(Integer id, Double newPrice)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER
