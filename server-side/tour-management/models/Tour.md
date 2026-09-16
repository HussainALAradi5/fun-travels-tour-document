# Tour Model

**Table:** `tours`
**File:** `src/main/java/com/server/server/Models/tourmanagement/Tour.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| tourNumber | String | Unique, Generated | Auto-generated tour code |
| title | String | Not Blank | Tour title |
| description | String | - | Tour description |
| basePrice | BigDecimal | Not Null | Base price per person |
| numberOfDays | Integer | Not Null | Duration in days |
| startDate | LocalDate | Not Null | Tour start date |
| endDate | LocalDate | Not Null | Tour end date |
| maxCapacity | Integer | Not Null | Maximum passengers |
| availableSlots | Integer | - | Remaining slots |
| status | GenericStatus | Not Null | Workflow status |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| startCountry | Country | ManyToOne | Departure country |
| endCountry | Country | ManyToOne | Destination country |
| startCity | City | ManyToOne | Departure city |
| endCity | City | ManyToOne | Destination city |
| destinationCountries | Country | ManyToMany | All destinations |
| agency | Agency | ManyToOne | Managing agency |
| agencyBranch | AgencyBranch | ManyToOne | Managing branch |
| transportation | Transportation | ManyToOne | Assigned transport |
| mealPlans | MealPlan | ManyToMany | Available meals |
| tickets | Ticket | OneToMany | Generated tickets |
| reservations | TourReservation | OneToMany | Tour reservations |

## Status Workflow
```
PENDING -> APPROVED -> ACTIVE -> COMPLETED
                \-> REJECTED
         \-> CANCELLED
```
