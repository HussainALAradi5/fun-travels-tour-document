# MealPlan

Table `meal_plans`. Inherits `BaseEntity`. Source: `models/tourmanagement/MealPlan.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `mealName` | `String` |  required |
| `mealPrice` | `Double` |  required |
| `mealDescription` | `String` |   |
| `isVegetarian` | `boolean` |   |
| `isVegan` | `boolean` |   |
| `isGlutenFree` | `boolean` |   |
| `spiceLevel` | `SpiceLevel` |  required |
| `status` | `GenericStatus` |  required |
| `agency` | `Agency` | ManyToOne  |
