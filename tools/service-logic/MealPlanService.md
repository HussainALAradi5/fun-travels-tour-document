## Business logic

- `findAll` is public: admins see every meal, agency staff their agency's meals plus shared ones (no agency), visitors and customers only shared meals.
- Agency staff create meals for their own agency; admins may name an agency or create a shared meal.
- `updateMeal` replaces name, price, description, diets, and spice level; the owning agency never changes. VEGAN implies VEGETARIAN; STANDARD cannot be combined with another diet. Edit, status, and price changes are limited to the meal's agency (shared meals: admins only).
- A missing meal is 404. Inactive meals cannot be added to tours or booked, and tour responses only list active meals.
