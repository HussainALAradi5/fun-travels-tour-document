# Ticket Model

**Table:** `tickets`
**File:** `src/main/java/com/server/server/Models/tourmanagement/Ticket.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| ticketNumber | String | Unique, Generated | Auto-generated code |
| guestCount | Integer | Not Null | Number of guests |
| unitPrice | BigDecimal | - | Price per unit |
| totalPrice | BigDecimal | Not Null | Total price |
| discountAmount | BigDecimal | Default: 0 | Applied discount |
| bookingDate | LocalDate | Not Null | Booking date |
| paid | boolean | Default: false | Payment status |
| ticketStatus | TicketStatus | Not Null | PENDING, CONFIRMED, CANCELLED, COMPLETED |
| approvalStatus | GenericStatus | - | Admin approval status |
| hasMealPlan | boolean | Default: false | Meal plan selected |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| customer | User | ManyToOne | Ticket holder |
| tour | Tour | ManyToOne | Associated tour |
| assignedSeat | Seat | ManyToOne | Assigned seat |
| transportation | Transportation | ManyToOne | Transport unit |
| destinationCity | City | ManyToOne | Destination |
| selectedMeals | MealPlan | ManyToMany | Selected meals |
