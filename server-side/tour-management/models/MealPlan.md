# MealPlan Model

**Table:** `meal_plans`
**File:** `src/main/java/com/server/server/Models/tourmanagement/MealPlan.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| mealName | String | Not Blank | Meal name |
| mealPrice | BigDecimal | Not Null | Price per meal |
| mealDescription | String | - | Description |
| isVegetarian | boolean | Default: false | Vegetarian flag |
| isVegan | boolean | Default: false | Vegan flag |
| isGlutenFree | boolean | Default: false | Gluten-free flag |
| status | GenericStatus | Not Null | ACTIVE, INACTIVE |
