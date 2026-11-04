# tourmanagement DTOs

Source: `dto/tourmanagement/`. Clients mirror these in `src/dtos/tour-management/`.

## MealPlanCreateRequest

request record. A meal package; the spice level defaults to NONE.

| Field | Type | Rules |
| --- | --- | --- |
| `mealName` | `String` | required, not blank |
| `mealPrice` | `Double` | required; Meal price cannot be negative |
| `mealDescription` | `String` | - |
| `dietaryTypes` | `Set<MealDietaryType>` | - |
| `spiceLevel` | `SpiceLevel` | - |
| `agencyId` | `Integer` | - |

## MealPlanResponse

response record; built by `from(MealPlan)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `mealName` | `String` | - |
| `mealPrice` | `Double` | - |
| `mealDescription` | `String` | - |
| `dietaryTypes` | `Set<MealDietaryType>` | - |
| `spiceLevel` | `SpiceLevel` | - |
| `status` | `GenericStatus` | - |

## ReservationCreateRequest

request record. Creates a reservation. Customers always book for themselves; staff pass `user`. When `tickets` is empty the server issues `requestedSlots` tickets without seat or meal choices.

| Field | Type | Rules |
| --- | --- | --- |
| `tour` | `EntityReference` | required; nested values validated |
| `user` | `EntityReference` | nested values validated |
| `requestedSlots` | `Integer` | requestedSlots must be at least 1; A reservation can hold at most 20 travelers |
| `tickets` | `List<TicketSelectionRequest>` | A reservation can hold at most 20 travelers; nested values validated |

## ReservationFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| (inherited) | `GenericFilterRequest` | `page`, `size`, `search`, `sortBy`, `sortDir` |
| `status` | `GenericStatus` | optional |
| `customerId` | `Long` | optional |
| `agencyId` | `Long` | optional |
| `startDate` | `LocalDate` | optional |
| `endDate` | `LocalDate` | optional |

## ReservationResponse

response record; built by `from(TourReservation)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `reservationNumber` | `String` | - |
| `tour` | `TourSummary` | - |
| `user` | `UserSummary` | - |
| `requestedSlots` | `Integer` | - |
| `totalPrice` | `BigDecimal` | - |
| `status` | `GenericStatus` | - |
| `bookingDate` | `LocalDateTime` | - |
| `holdExpiresAt` | `LocalDateTime` | - |

## ReservationSummary

response record; built by `from(TourReservation)`. A reservation by id and number.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `reservationNumber` | `String` | - |

## SeatFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| (inherited) | `GenericFilterRequest` | `page`, `size`, `search`, `sortBy`, `sortDir` |
| `transportId` | `Integer` | optional |
| `tourId` | `Integer` | optional |
| `status` | `SeatStatus` | optional |
| `chairType` | `ChairType` | optional |
| `keyword` | `String` | optional |

## SeatResponse

response record; built by `from(Seat)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `seatCode` | `String` | - |
| `chairType` | `ChairType` | - |
| `status` | `SeatStatus` | - |
| `seatPriceModifier` | `Double` | - |

## SeatSummary

response record; built by `from(Seat)`. A seat with its chair type and fleet status (AVAILABLE or MAINTENANCE).

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `seatCode` | `String` | - |
| `chairType` | `ChairType` | - |
| `status` | `SeatStatus` | - |

## SeatUpdateRequest

request record. Seat configuration; null fields are left unchanged.

| Field | Type | Rules |
| --- | --- | --- |
| `chairType` | `ChairType` | - |
| `status` | `SeatStatus` | - |
| `seatPriceModifier` | `Double` | - |

## TicketCreateRequest

request record. Staff-issued single ticket outside a reservation (walk-in sale), with the traveler's optional seat and meals.

| Field | Type | Rules |
| --- | --- | --- |
| `tour` | `EntityReference` | required; nested values validated |
| `customer` | `EntityReference` | required; nested values validated |
| `assignedSeat` | `EntityReference` | nested values validated |
| `selectedMeals` | `List<EntityReference>` | nested values validated |

## TicketFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| (inherited) | `GenericFilterRequest` | `page`, `size`, `search`, `sortBy`, `sortDir` |
| `status` | `TicketStatus` | optional |
| `customerId` | `Long` | optional |
| `tourId` | `Integer` | optional |
| `reservationId` | `Integer` | optional |
| `startDate` | `LocalDate` | optional |
| `endDate` | `LocalDate` | optional |

## TicketResponse

response record; built by `from(Ticket)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `ticketNumber` | `String` | - |
| `customer` | `UserSummary` | - |
| `tour` | `TourSummary` | - |
| `assignedSeat` | `SeatSummary` | - |
| `basePrice` | `BigDecimal` | - |
| `discountPrice` | `BigDecimal` | - |
| `seatPriceModifier` | `BigDecimal` | - |
| `totalPrice` | `BigDecimal` | - |
| `bookingDate` | `LocalDateTime` | - |
| `paid` | `boolean` | - |
| `ticketStatus` | `TicketStatus` | - |
| `approvalStatus` | `GenericStatus` | - |
| `hasMealPlan` | `boolean` | - |
| `qrCode` | `String` | - |
| `barcode` | `String` | - |
| `createdAt` | `LocalDateTime` | - |

## TicketSelectionRequest

request record. One traveler's optional seat and meal choices. Prices are calculated by the server.

| Field | Type | Rules |
| --- | --- | --- |
| `assignedSeat` | `EntityReference` | nested values validated |
| `selectedMeals` | `List<EntityReference>` | nested values validated |

## TourCreateRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `tourNumber` | `String` | required, not blank |
| `title` | `String` | required, not blank |
| `description` | `String` | - |
| `basePrice` | `Double` | required |
| `numberOfDays` | `Integer` | required |
| `startDate` | `LocalDate` | required |
| `endDate` | `LocalDate` | - |
| `maxCapacity` | `Integer` | required |
| `startCountryId` | `Integer` | required |
| `endCountryId` | `Integer` | required |
| `startCityId` | `Integer` | required |
| `endCityId` | `Integer` | required |
| `destinationCountryIds` | `List<Integer>` | - |
| `transportationId` | `Integer` | - |
| `mealPlanIds` | `List<Integer>` | - |

## TourFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| (inherited) | `GenericFilterRequest` | `page`, `size`, `search`, `sortBy`, `sortDir` |
| `status` | `GenericStatus` | optional |
| `minSlots` | `Integer` | optional |
| `startDate` | `LocalDate` | optional |
| `endDate` | `LocalDate` | optional |
| `agencyId` | `Long` | optional |
| `branchId` | `Long` | optional |
| `minPrice` | `Double` | optional |
| `maxPrice` | `Double` | optional |
| `countryId` | `Integer` | optional |
| `cityId` | `Integer` | optional |
| `createdById` | `Integer` | optional |

## TourResponse

response record; built by `from(Tour)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `tourNumber` | `String` | - |
| `title` | `String` | - |
| `description` | `String` | - |
| `basePrice` | `Double` | - |
| `discountPrice` | `Double` | - |
| `totalPrice` | `Double` | - |
| `numberOfDays` | `Integer` | - |
| `startDate` | `LocalDate` | - |
| `endDate` | `LocalDate` | - |
| `maxCapacity` | `Integer` | - |
| `availableSlots` | `Integer` | - |
| `status` | `GenericStatus` | - |
| `hasTransportation` | `boolean` | - |
| `startCountry` | `CountrySummary` | - |
| `endCountry` | `CountrySummary` | - |
| `destinationCountries` | `List<CountrySummary>` | - |
| `startCity` | `CitySummary` | - |
| `endCity` | `CitySummary` | - |
| `agency` | `AgencySummary` | - |
| `agencyBranch` | `BranchSummary` | - |
| `transportation` | `TransportationSummary` | - |
| `createdBy` | `UserSummary` | - |
| `createdAt` | `LocalDateTime` | - |
| `availableMeals` | `List<MealPlanResponse>` | - |

## TourSummary

response record; built by `from(Tour)`. A tour as tickets and reservations show it, with its travel dates.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `tourNumber` | `String` | - |
| `title` | `String` | - |
| `startDate` | `LocalDate` | - |
| `endDate` | `LocalDate` | - |

## TourUpdateRequest

request record. Partial tour update: null fields are left unchanged. References are `{ "id": n `}.

| Field | Type | Rules |
| --- | --- | --- |
| `title` | `String` | - |
| `tourNumber` | `String` | - |
| `description` | `String` | - |
| `basePrice` | `Double` | Base price cannot be negative |
| `startDate` | `LocalDate` | - |
| `endDate` | `LocalDate` | - |
| `numberOfDays` | `Integer` | Number of days must be positive |
| `maxCapacity` | `Integer` | Capacity must be positive |
| `startCountry` | `EntityReference` | - |
| `endCountry` | `EntityReference` | - |
| `startCity` | `EntityReference` | - |
| `endCity` | `EntityReference` | - |
| `transportation` | `EntityReference` | - |
| `destinationCountries` | `List<EntityReference>` | - |
| `availableMeals` | `List<EntityReference>` | - |

## TransportationCreateRequest

request record.

| Field | Type | Rules |
| --- | --- | --- |
| `transportationNumber` | `String` | required, not blank |
| `code` | `String` | required, not blank |
| `type` | `TransportationType` | required |
| `providerName` | `String` | required, not blank |
| `totalCapacity` | `Integer` | required; Capacity must be at least 1 |
| `agencyId` | `Integer` | required |
| `branchId` | `Integer` | - |
| `seatConfig` | `Map<String, Integer>` | - |

## TransportationFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| (inherited) | `GenericFilterRequest` | `page`, `size`, `search`, `sortBy`, `sortDir` |
| `type` | `TransportationType` | optional |
| `status` | `GenericStatus` | optional |
| `unitStatus` | `TransportationStatus` | optional |
| `keyword` | `String` | optional |

## TransportationResponse

response record; built by `from(Transportation)`, `listItem(Transportation)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `transportationNumber` | `String` | - |
| `code` | `String` | - |
| `type` | `TransportationType` | - |
| `providerName` | `String` | - |
| `status` | `GenericStatus` | - |
| `unitStatus` | `TransportationStatus` | - |
| `totalCapacity` | `Integer` | - |
| `agency` | `AgencySummary` | - |
| `agencyBranch` | `BranchSummary` | - |
| `seats` | `List<SeatSummary>` | - |

## TransportationSummary

response record; built by `from(Transportation)`. The vehicle assigned to a tour.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `transportationNumber` | `String` | - |
| `type` | `TransportationType` | - |

## TransportationUpdateRequest

request record. Editable vehicle fields. Code and capacity are permanent; `seatConfig` re-labels chair types.

| Field | Type | Rules |
| --- | --- | --- |
| `transportationNumber` | `String` | - |
| `providerName` | `String` | - |
| `type` | `TransportationType` | - |
| `seatConfig` | `Map<String, Integer>` | - |
