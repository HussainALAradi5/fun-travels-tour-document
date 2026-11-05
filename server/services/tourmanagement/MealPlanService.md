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

**Exceptions:** none of its own; failures come from the functions it calls.

### `MealPlan findById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Meal not found | `ResourceNotFoundException` | 404 |

### `PageResponse<MealPlan> getAgencyCatalog(Integer agencyId, Integer page, Integer size)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `MealPlan createMeal(MealPlanCreateRequest request)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Agency not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Standard cannot be combined with another dietary classification. | `IllegalArgumentException` | 400 |

### `MealPlan updateMeal(Integer id, MealPlanCreateRequest request)`

**Purpose:** Replaces a meal's name, price, description, diets, and spice level. The owning agency never changes.

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Meal not found | `ResourceNotFoundException` | 404 |
| Standard cannot be combined with another dietary classification. | `IllegalArgumentException` | 400 |

### `void updateMealStatus(Integer id, GenericStatus status)`

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Meal not found | `ResourceNotFoundException` | 404 |
