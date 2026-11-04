# MealPlanService

Source: `services/tourmanagement/MealPlanService.java`.

## Business logic

- `findAll` is public: admins see every meal, agency staff their agency's meals plus shared ones (no agency), visitors and customers only shared meals.
- Agency staff create meals for their own agency; admins may name an agency or create a shared meal.
- `updateMeal` replaces name, price, description, diets, and spice level; the owning agency never changes. VEGAN implies VEGETARIAN; STANDARD cannot be combined with another diet. Edit, status, and price changes are limited to the meal's agency (shared meals: admins only).
- A missing meal is 404. Inactive meals cannot be added to tours or booked, and tour responses only list active meals.

## Functions

### `PageResponse<MealPlan> findAll(Integer page, Integer size, String sortDir)`

**Purpose:** Admins see every meal; agency staff see their agency's meals and shared ones; everyone else sees shared ones.

**Runs in:** read-only transaction

### `MealPlan findById(Integer id)`

**Runs in:** read-only transaction

### `PageResponse<MealPlan> getAgencyCatalog(Integer agencyId, Integer page, Integer size)`

**Runs in:** read-only transaction

### `MealPlan createMeal(MealPlanCreateRequest request)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `MealPlan updateMeal(Integer id, MealPlanCreateRequest request)`

**Purpose:** Replaces a meal's name, price, description, diets, and spice level. The owning agency never changes.

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `void updateMealStatus(Integer id, GenericStatus status)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `MealPlan updatePricing(Integer id, Double newPrice)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER
