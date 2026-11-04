# Tour

Table `tours`. Inherits `BaseEntity`. Source: `models/tourmanagement/Tour.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `tourNumber` | `String` |  unique, required |
| `title` | `String` |  required |
| `description` | `String` |   |
| `startDate` | `LocalDate` |  required |
| `endDate` | `LocalDate` |   |
| `numberOfDays` | `Integer` |   |
| `maxCapacity` | `Integer` |  required |
| `availableSlots` | `Integer` |   |
| `status` | `GenericStatus` |  required |
| `hasTransportation` | `boolean` |  required |
| `transportation` | `Transportation` | ManyToOne  |
| `startCountry` | `Country` | ManyToOne required |
| `endCountry` | `Country` | ManyToOne required |
| `startCity` | `City` | ManyToOne required |
| `endCity` | `City` | ManyToOne required |
| `destinationCountries` | `Set<Country>` | ManyToMany  |
| `agency` | `Agency` | ManyToOne  |
| `agencyBranch` | `AgencyBranch` | ManyToOne  |
| `tickets` | `List<Ticket>` | OneToMany  |
| `reservations` | `List<TourReservation>` | OneToMany  |
| `basePrice` | `Double` |  required |
| `discountPrice` | `Double` |   |
| `totalPrice` | `Double` |   |
| `availableMeals` | `Set<MealPlan>` | ManyToMany  |
