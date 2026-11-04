# Models

Every persisted model extends [BaseEntity](base/BaseEntity.md): `id`, unique `code`, `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. Equality is by type and id.

| Domain | Model | Table | Inherits |
| --- | --- | --- | --- |
| agency | [Agency](agency/Agency.md) | `agencies` | BaseEntity |
| agency | [AgencyBranch](agency/AgencyBranch.md) | `agency_branch` | BaseEntity |
| base | [BaseEntity](base/BaseEntity.md) | `(mapped superclass)` | - |
| geography | [City](geography/City.md) | `cities` | BaseEntity |
| geography | [Country](geography/Country.md) | `countries` | BaseEntity |
| geography | [Port](geography/Port.md) | `ports` | BaseEntity |
| notification | [Notification](notification/Notification.md) | `notifications` | BaseEntity |
| payment | [Account](payment/Account.md) | `accounts` | BaseEntity |
| payment | [Payment](payment/Payment.md) | `payments` | BaseEntity |
| payment | [Transaction](payment/Transaction.md) | `transactions` | BaseEntity |
| support | [GenericComment](support/GenericComment.md) | `generic_comments` | BaseEntity |
| support | [GenericEventLog](support/GenericEventLog.md) | `generic_event_logs` | BaseEntity |
| support | [UserRequest](support/UserRequest.md) | `user_requests` | BaseEntity |
| tourmanagement | [MealPlan](tourmanagement/MealPlan.md) | `meal_plans` | BaseEntity |
| tourmanagement | [Seat](tourmanagement/Seat.md) | `seats` | BaseEntity |
| tourmanagement | [Ticket](tourmanagement/Ticket.md) | `tickets` | BaseEntity |
| tourmanagement | [Tour](tourmanagement/Tour.md) | `tours` | BaseEntity |
| tourmanagement | [TourReservation](tourmanagement/TourReservation.md) | `tour_reservations` | BaseEntity |
| tourmanagement | [Transportation](tourmanagement/Transportation.md) | `transportations` | BaseEntity |
| user | [User](user/User.md) | `users` | BaseEntity |

## Relationships

| Model | Relation | Target | Field | Foreign key | Cascade |
| --- | --- | --- | --- | --- | --- |
| Agency | ManyToOne | User | `agencyOwner` | `owner_id` | - |
| Agency | ManyToOne | Country | `country` | `country_id` | - |
| Agency | ManyToOne | City | `city` | `city_id` | - |
| Agency | OneToMany | AgencyBranch | `branches` | mapped by `agency` | ALL |
| Agency | OneToMany | User | `employees` | mapped by `agency` | - |
| AgencyBranch | ManyToOne | Agency | `agency` | `agency_id` | - |
| AgencyBranch | ManyToOne | Country | `country` | `country_id` | - |
| AgencyBranch | ManyToOne | City | `city` | `city_id` | - |
| AgencyBranch | ManyToOne | User | `branchManager` | `manager_id` | - |
| AgencyBranch | OneToMany | User | `employees` | mapped by `agencyBranch` | - |
| BaseEntity | ManyToOne | User | `createdBy` | `created_by_id` | - |
| BaseEntity | ManyToOne | User | `updatedBy` | `updated_by_id` | - |
| City | ManyToOne | Country | `country` | `country_id` | - |
| Port | ManyToOne | City | `city` | `city_id` | - |
| Port | ManyToOne | Country | `country` | `country_id` | - |
| Notification | ManyToOne | User | `recipient` | `user_id` | - |
| Account | OneToOne | User | `user` | `user_id` | - |
| Payment | ManyToOne | TourReservation | `reservation` | `reservation_id` | - |
| Payment | OneToMany | Transaction | `transactions` | mapped by `payment` | ALL |
| Transaction | ManyToOne | Account | `account` | `account_id` | - |
| Transaction | ManyToOne | Payment | `payment` | `payment_id` | - |
| Transaction | ManyToOne | TourReservation | `reservation` | `reservation_id` | - |
| GenericComment | ManyToOne | User | `author` | `author_id` | - |
| GenericEventLog | ManyToOne | User | `actor` | `actor_id` | - |
| UserRequest | ManyToOne | User | `user` | `user_id` | - |
| UserRequest | ManyToOne | User | `assignedTo` | `assigned_to_id` | - |
| UserRequest | ManyToOne | User | `solvedBy` | `solved_by_id` | - |
| MealPlan | ManyToOne | Agency | `agency` | `agency_id` | - |
| Seat | ManyToOne | Transportation | `transportation` | `transportation_id` | - |
| Ticket | ManyToOne | Tour | `tour` | `tour_id` | - |
| Ticket | ManyToOne | User | `customer` | `customer_id` | - |
| Ticket | ManyToOne | Seat | `assignedSeat` | `seat_id` | - |
| Ticket | ManyToMany | MealPlan | `selectedMeals` | `ticket_id` | - |
| Ticket | ManyToOne | TourReservation | `reservation` | `reservation_id` | - |
| Tour | ManyToOne | Transportation | `transportation` | `transportation_id` | - |
| Tour | ManyToOne | Country | `startCountry` | `start_country_id` | - |
| Tour | ManyToOne | Country | `endCountry` | `end_country_id` | - |
| Tour | ManyToOne | City | `startCity` | `start_city_id` | - |
| Tour | ManyToOne | City | `endCity` | `end_city_id` | - |
| Tour | ManyToMany | Country | `destinationCountries` | `tour_id` | - |
| Tour | ManyToOne | Agency | `agency` | `agency_id` | - |
| Tour | ManyToOne | AgencyBranch | `agencyBranch` | `branch_id` | - |
| Tour | OneToMany | Ticket | `tickets` | mapped by `tour` | ALL |
| Tour | OneToMany | TourReservation | `reservations` | mapped by `tour` | ALL |
| Tour | ManyToMany | MealPlan | `availableMeals` | `tour_id` | - |
| TourReservation | ManyToOne | Tour | `tour` | `tour_id` | - |
| TourReservation | OneToMany | Ticket | `tickets` | mapped by `reservation` | ALL |
| TourReservation | OneToMany | Transaction | `transactions` | mapped by `reservation` | ALL |
| TourReservation | OneToMany | Payment | `payments` | mapped by `reservation` | ALL |
| Transportation | OneToMany | Tour | `tours` | mapped by `transportation` | - |
| Transportation | ManyToOne | Agency | `agency` | `agency_id` | - |
| Transportation | ManyToOne | AgencyBranch | `agencyBranch` | `agency_branch_id` | - |
| Transportation | OneToMany | Seat | `seats` | mapped by `transportation` | ALL |
| User | ManyToOne | Agency | `agency` | `agency_id` | - |
| User | ManyToOne | AgencyBranch | `agencyBranch` | `agency_branch_id` | - |
| User | OneToOne | Account | `account` | mapped by `user` | ALL |
