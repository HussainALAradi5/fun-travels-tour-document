# Endpoint Reference

This catalog maps every controller route to its purpose and implementing service function. Responses use `ApiResponse<T>` unless stated otherwise. Detailed business failures belong to the linked service documentation.

## Authentication

| Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|
| `POST` | `/api/auth/register` | Create a customer account. | Validated `User` body | `UserService` | `createUser` |
| `POST` | `/api/auth/login` | Authenticate and issue a JWT. | Email/identifier and password map | `AuthService`, `UserService`, `JwtService` | `authenticate`, `login`, `generateToken` |

## Users and accounts

| Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|
| `GET` | `/api/users` | List users for administration. | None | `UserService` | Repository-backed user listing |
| `GET` | `/api/users/{id}` | View one user. | User ID | `UserService` | `getUserById` |
| `GET` | `/api/users/agency/{agencyId}` | List agency staff, optionally by role. | Agency ID, optional `type` | `UserService` | `getAgencyUsers` |
| `PUT` | `/api/users/{id}` | Update a user profile. | User ID and validated `User` | `UserService` | `updateUser` |
| `POST` | `/api/users/bulk-import` | Import multiple employees. | Multipart file and `agencyId` | `UserService` | `bulkImportEmployees` |
| `PUT` | `/api/users/permissions/{id}` | Change role and branch assignment. | User ID, `type`, optional `branchId` | `UserService` | `updatePermissions` |
| `POST` | `/api/users/add-employee` | Create an employee account. | Validated `User` | `UserService` | `createUser` |
| `DELETE` | `/api/users/{id}` | Deactivate a user without deleting history. | User ID | `UserService` | `softDeleteUser` |
| `GET` | `/api/users/role/{type}` | Find users by application role. | `UserTypeEnum` | `UserService` | `getUsersByType` |
| `POST` | `/api/users/request-password-reset` | Send a reset link. | Email and base URL | `UserService` | `requestPasswordReset` |
| `POST` | `/api/users/confirm-password-reset` | Consume a reset token and set a password. | Identifier, token, base number, new password | `UserService` | `confirmPasswordReset` |
| `GET` | `/api/accounts/user/{userId}/balance` | Show wallet/account balance. | User ID | `AccountService` | `getAccountByUserId` |
| `GET` | `/api/accounts/user/{userId}/history` | Show wallet transaction history. | User ID | `AccountService` | `getTransactionHistory` |
| `GET` | `/api/wallet/config` | Supply publishable payment configuration. | None | Controller configuration | `getStripeConfig` |
| `POST` | `/api/wallet/top-up` | Add externally paid funds to a wallet. | Amount, method, optional Stripe token | `WalletTopUpService` | `processWalletTopUp` |

## Agencies and branches

| Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|
| `POST` | `/api/agencies` | Create an agency and resolve owner/geography references. | Agency payload map | `AgencyService` | `createAgencyFromMap` |
| `GET` | `/api/agencies/{id}` | View one agency. | Numeric agency ID | `AgencyService` | `getAgencyById` |
| `GET` | `/api/agencies/search` | Power the paginated remote agency selector. | `query`, `page`, `size` | `AgencyService` | `searchAgencies` |
| `GET` | `/api/agencies/{id}/employees` | List active agency employees. | Numeric agency ID | `AgencyService` | `getEmployeesByAgencyId` |
| `GET` | `/api/agencies` | Return the legacy complete agency list. | None | `AgencyService` | `getAllAgencies` |
| `POST` | `/api/branches/agency/{agencyId}` | Add a branch to an agency. | Numeric agency ID and branch body | `AgencyBranchService` | `addBranch` |
| `GET` | `/api/branches` | List every branch. | None | `AgencyBranchService` | `getAllBranches` |
| `GET` | `/api/branches/agency/{agencyId}` | List active branches for an agency. | Numeric agency ID | `AgencyBranchService` | `getBranchesByAgency` |
| `GET` | `/api/branches/agency/{agencyId}/search` | Power the paginated remote branch selector. | Agency ID, `query`, `page`, `size` | `AgencyBranchService` | `searchBranches` |
| `GET` | `/api/branches/agency/{agencyId}/branch/{branchId}/employees` | List branch employees after ownership validation. | Agency and branch IDs | `AgencyBranchService` | `getEmployeesByBranch` |

## Tours, transportation, seats, and meals

| Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|
| `GET` | `/api/tours/catalog` | Browse currently bookable tours. | Geography/date filters and pagination | `TourService` | `getCatalogTours` |
| `GET` | `/api/tours/search` | Search operational tours. | `TourFilterRequest` | `TourService` | `filter` |
| `GET` | `/api/tours` | List tours with bounded pagination. | Page, size, sort | `TourService` | `getAll` |
| `GET` | `/api/tours/{id}` | View one tour. | Tour ID | `TourService` | `getById` |
| `POST` | `/api/tours` | Create and validate a tour. | Validated `Tour` | `TourService` | `create` |
| `PUT` | `/api/tours/{id}` | Update editable tour details. | Tour ID and validated `Tour` | `TourService` | `updateTour` |
| `PUT` | `/api/tours/{id}/status` | Execute a tour workflow transition. | Tour ID and status | `TourService` | `updateStatus` |
| `POST` | `/api/transportations` | Register a unit and generate its seats. | `TransportationCreateRequest` | `TransportationService` | `create` |
| `POST` | `/api/transportations/imports` | Import multiple transport units server-side. | Multipart Excel file | `TransportationService` | `importExcel` |
| `GET` | `/api/transportations` | List transport units. | Page, size, sort | `TransportationService` | `getAll` |
| `GET` | `/api/transportations/{id}` | View a unit with seat details. | Transportation ID | `TransportationService` | `getById` |
| `PUT` | `/api/transportations/{id}` | Update scalar fields or safe seat layout. | ID and `Transportation` | `TransportationService` | `update` |
| `PATCH` | `/api/transportations/{id}/status` | Change operational unit status. | ID and `TransportationStatus` | `TransportationService` | `updateStatus` |
| `GET` | `/api/transportations/search` | Search the fleet using server filters. | `TransportationFilterRequest` | `TransportationService` | `filter` |
| `GET` | `/api/seats` | List seats with pagination. | Page, size, direction | `SeatService` | `getAll` |
| `GET` | `/api/seats/{id}` | View one seat. | Seat ID | `SeatService` | `getById` |
| `PATCH` | `/api/seats/{id}` | Configure an editable seat. | Seat ID and validated seat body | `SeatService` | `updateSeat` |
| `GET` | `/api/seats/search` | Filter seats by unit, class, status, or code. | `SeatFilterRequest` | `SeatService` | `filter` |
| `PATCH` | `/api/seats/{id}/status` | Change operational seat status. | Seat ID and `SeatStatus` | `SeatService` | `updateStatus` |
| `GET` | `/api/meals` | List meal plans. | Page, size, direction | `MealPlanService` | `findAll` |
| `GET` | `/api/meals/agency/{agencyId}` | Show an agency meal catalog. | Agency ID and pagination | `MealPlanService` | `getAgencyCatalog` |
| `POST` | `/api/meals` | Define a meal offering. | Validated `MealPlan` | `MealPlanService` | `createMeal` |
| `PATCH` | `/api/meals/{id}/status` | Enable or disable a meal. | Meal ID and status | `MealPlanService` | `updateMealStatus` |
| `PUT` | `/api/meals/{id}/price` | Update meal pricing. | Meal ID and price | `MealPlanService` | `updatePricing` |

## Reservations, tickets, and payments

| Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|
| `POST` | `/api/reservations` | Create a 15-minute booking hold. | Validated reservation and tickets | `TourReservationService` | `create` |
| `PATCH` | `/api/reservations/{id}/status` | Perform an authorized reservation transition. | ID and status | `TourReservationService` | `updateStatus` |
| `PATCH` | `/api/reservations/{id}/cancel` | Cancel, refund when eligible, and release inventory. | Reservation ID | `TourReservationService` | `cancelReservation` |
| `GET` | `/api/reservations/search` | Search reservations with role scoping. | `ReservationFilterRequest` | `TourReservationService` | `filter` |
| `GET` | `/api/reservations` | List role-scoped reservations. | Page, size, direction | `TourReservationService` | `getAll` |
| `GET` | `/api/reservations/{id}` | View one authorized reservation. | Reservation ID | `TourReservationService` | `getById` |
| `GET` | `/api/tickets/search` | Search role-scoped tickets. | `TicketFilterRequest` | `TicketService` | `filter` |
| `GET` | `/api/tickets` | List role-scoped tickets. | Page, size, direction | `TicketService` | `getAll` |
| `GET` | `/api/tickets/{id}` | View one authorized ticket. | Ticket ID | `TicketService` | `getById` |
| `POST` | `/api/tickets` | Create a ticket and generate codes. | Validated `Ticket` | `TicketService` | `create` |
| `PUT` | `/api/tickets/{id}/status` | Execute a ticket approval transition. | ID and status | `TicketService` | `updateStatus` |
| `PUT` | `/api/tickets/{id}/cancel` | Cancel a ticket and release its inventory. | Ticket ID | `TicketService` | `cancelTicket` |
| `PUT` | `/api/tickets/{id}/approve` | Approve a paid ticket. | Ticket ID | `TicketService` | `approveTicket` |
| `PUT` | `/api/tickets/{id}/confirm` | Confirm an approved ticket. | Ticket ID | `TicketService` | `confirmTicket` |
| `POST` | `/api/payments/execute/{reservationId}` | Pay and finalize a held reservation. | Reservation ID and payment method | `TourReservationService` | `finalizeReservationWithPayment` |
| `GET` | `/api/payments` | Search payments by owner, status, method, or dates. | `PaymentFilterRequest` | `PaymentService` | `filter` |
| `GET` | `/api/payments/{id}` | View one authorized payment. | Payment ID | `PaymentService` | `getById` |
| `GET` | `/api/transactions` | Search account transactions. | `TransactionFilterRequest` | `TransactionService` | `filterTransactions` |
| `GET` | `/api/transactions/{id}` | View one authorized transaction. | Transaction ID | `TransactionService` | `getById` |
| `POST` | `/api/transactions/manual-credit/{userId}` | Apply an administrative wallet credit. | User ID, amount, description | `AccountService`, `TransactionService` | `getAccountByUserId`, `creditAccount` |

## Geography

| Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|
| `GET` | `/api/countries` | Populate country selection. | None | `CountryService` | `getAllCountries` |
| `POST` | `/api/countries` | Add a country manually. | `Country` body | `CountryService` | `createCountry` |
| `POST` | `/api/countries/sync/{name}` | Import one country from the external provider. | Country name | `CountryService` | `syncFromExternal` |
| `POST` | `/api/countries/sync-all` | Synchronize the country catalog. | None | `CountryService` | `syncAllCountries` |
| `DELETE` | `/api/countries/{id}` | Remove a country. | Country ID | `CountryService` | `deleteCountry` |
| `GET` | `/api/cities` | Populate city selection. | None | `CityService` | `getAllCities` |
| `GET` | `/api/cities/country/{countryId}` | Return cities within a country. | Country ID | `CityService` | `getCitiesByCountry` |
| `POST` | `/api/cities` | Add a city. | `City` body | `CityService` | `createCity` |
| `DELETE` | `/api/cities/{id}` | Remove a city. | City ID | `CityService` | `deleteCity` |
| `GET` | `/api/ports` | List active transport ports. | None | `PortService` | `getAllActivePorts` |
| `POST` | `/api/ports` | Create a transport port. | Validated `Port` | `PortService` | `createPort` |
| `PUT` | `/api/ports/{id}/status` | Change port lifecycle status. | Port ID and status | `PortService` | `updateStatus` |

## Notifications and support

| Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|
| `GET` | `/api/notifications/user/{userId}` | Show a user's notifications. | User ID | `NotificationService` | `getUserNotifications` |
| `PUT` | `/api/notifications/{id}/read` | Mark a notification read. | Notification ID | `NotificationService` | `markAsRead` |
| `GET` | `/api/notifications/user/{userId}/counts` | Show unread/total counters. | User ID | `NotificationService` | `getNotificationCounts` |
| `POST` | `/api/user-requests` | Open a support request. | Validated `UserRequest` | `UserRequestService` | `create` |
| `GET` | `/api/user-requests` | Search support requests. | `UserRequestFilterRequest` | `UserRequestService` | `getFilteredRequests` |
| `GET` | `/api/user-requests/{id}` | View one request. | Request ID | `UserRequestService` | `getById` |
| `PATCH` | `/api/user-requests/{id}/assign/{agentId}` | Assign support ownership. | Request and agent IDs | `UserRequestService` | `assignRequest` |
| `PATCH` | `/api/user-requests/{id}/solve/{solverId}` | Resolve a support request. | Request and solver IDs | `UserRequestService` | `solveRequest` |
| `PATCH` | `/api/user-requests/{id}/reject/{rejectedById}` | Reject a support request. | Request and actor IDs | `UserRequestService` | `rejectRequest` |
| `DELETE` | `/api/user-requests/{id}` | Delete an eligible request. | Request ID | `UserRequestService` | `delete` |
| `GET` | `/api/tracking/{refType}/{refId}` | Read comments and event history for a domain record. | Reference type and ID | `GenericTrackingService` | `getTimelineMap` |
| `POST` | `/api/tracking/{refType}/{refId}/comments` | Add an auditable comment. | Reference, content, user ID | `GenericTrackingService` | `addComment` |
| `PUT` | `/api/tracking/comments/{commentId}` | Edit the author's comment. | Comment ID, editor ID, content | `GenericTrackingService` | `updateComment` |
