# Tour and Booking Management Endpoints

This table is the feature-owned HTTP contract. Business rules and exception details are documented in this folder's service pages.

| ID | Method | Endpoint | Why it is used | Request data | Service | Function |
|---|---|---|---|---|---|---|
| EP-1 | `GET` | `/api/tours/catalog` | Browse currently bookable tours. | Geography/date filters and pagination | `TourService` | `getCatalogTours` |
| EP-2 | `GET` | `/api/tours/search` | Search operational tours. | `TourFilterRequest` | `TourService` | `filter` |
| EP-3 | `GET` | `/api/tours` | List tours with bounded pagination. | Page, size, sort | `TourService` | `getAll` |
| EP-4 | `GET` | `/api/tours/{id}` | View one tour. | Tour ID | `TourService` | `getById` |
| EP-5 | `POST` | `/api/tours` | Create and validate a tour. | Validated `Tour` | `TourService` | `create` |
| EP-6 | `PUT` | `/api/tours/{id}` | Update editable tour details. | Tour ID and validated `Tour` | `TourService` | `updateTour` |
| EP-7 | `PUT` | `/api/tours/{id}/status` | Execute a tour workflow transition. | Tour ID and status | `TourService` | `updateStatus` |
| EP-8 | `POST` | `/api/transportations` | Register a unit and generate its seats. | `TransportationCreateRequest` | `TransportationService` | `create` |
| EP-9 | `POST` | `/api/transportations/imports` | Import multiple transport units server-side. | Multipart Excel file | `TransportationService` | `importExcel` |
| EP-10 | `GET` | `/api/transportations` | List transport units. | Page, size, sort | `TransportationService` | `getAll` |
| EP-11 | `GET` | `/api/transportations/{id}` | View a unit with seat details. | Transportation ID | `TransportationService` | `getById` |
| EP-12 | `PUT` | `/api/transportations/{id}` | Update scalar fields or safe seat layout. | ID and `Transportation` | `TransportationService` | `update` |
| EP-13 | `PATCH` | `/api/transportations/{id}/status` | Change operational unit status. | ID and `TransportationStatus` | `TransportationService` | `updateStatus` |
| EP-14 | `GET` | `/api/transportations/search` | Search the fleet using server filters. | `TransportationFilterRequest` | `TransportationService` | `filter` |
| EP-15 | `GET` | `/api/seats` | List seats with pagination. | Page, size, direction | `SeatService` | `getAll` |
| EP-16 | `GET` | `/api/seats/{id}` | View one seat. | Seat ID | `SeatService` | `getById` |
| EP-17 | `PATCH` | `/api/seats/{id}` | Configure an editable seat. | Seat ID and validated seat body | `SeatService` | `updateSeat` |
| EP-18 | `GET` | `/api/seats/search` | Filter seats by unit, class, status, or code. | `SeatFilterRequest` | `SeatService` | `filter` |
| EP-19 | `PATCH` | `/api/seats/{id}/status` | Change operational seat status. | Seat ID and `SeatStatus` | `SeatService` | `updateStatus` |
| EP-20 | `GET` | `/api/meals` | List meal plans. | Page, size, direction | `MealPlanService` | `findAll` |
| EP-21 | `GET` | `/api/meals/agency/{agencyId}` | Show an agency meal catalog. | Agency ID and pagination | `MealPlanService` | `getAgencyCatalog` |
| EP-22 | `POST` | `/api/meals` | Define a meal offering. | Validated `MealPlan` | `MealPlanService` | `createMeal` |
| EP-23 | `PATCH` | `/api/meals/{id}/status` | Enable or disable a meal. | Meal ID and status | `MealPlanService` | `updateMealStatus` |
| EP-24 | `PUT` | `/api/meals/{id}/price` | Update meal pricing. | Meal ID and price | `MealPlanService` | `updatePricing` |
| EP-25 | `POST` | `/api/reservations` | Create a 15-minute booking hold. | Validated reservation and tickets | `TourReservationService` | `create` |
| EP-26 | `PATCH` | `/api/reservations/{id}/status` | Perform an authorized reservation transition. | ID and status | `TourReservationService` | `updateStatus` |
| EP-27 | `PATCH` | `/api/reservations/{id}/cancel` | Cancel, refund when eligible, and release inventory. | Reservation ID | `TourReservationService` | `cancelReservation` |
| EP-28 | `GET` | `/api/reservations/search` | Search reservations with role scoping. | `ReservationFilterRequest` | `TourReservationService` | `filter` |
| EP-29 | `GET` | `/api/reservations` | List role-scoped reservations. | Page, size, direction | `TourReservationService` | `getAll` |
| EP-30 | `GET` | `/api/reservations/{id}` | View one authorized reservation. | Reservation ID | `TourReservationService` | `getById` |
| EP-31 | `GET` | `/api/tickets/search` | Search role-scoped tickets. | `TicketFilterRequest` | `TicketService` | `filter` |
| EP-32 | `GET` | `/api/tickets` | List role-scoped tickets. | Page, size, direction | `TicketService` | `getAll` |
| EP-33 | `GET` | `/api/tickets/{id}` | View one authorized ticket. | Ticket ID | `TicketService` | `getById` |
| EP-34 | `POST` | `/api/tickets` | Create a ticket and generate codes. | Validated `Ticket` | `TicketService` | `create` |
| EP-35 | `PUT` | `/api/tickets/{id}/status` | Execute a ticket approval transition. | ID and status | `TicketService` | `updateStatus` |
| EP-36 | `PUT` | `/api/tickets/{id}/cancel` | Cancel a ticket and release its inventory. | Ticket ID | `TicketService` | `cancelTicket` |
| EP-37 | `PUT` | `/api/tickets/{id}/approve` | Approve a paid ticket. | Ticket ID | `TicketService` | `approveTicket` |
| EP-38 | `PUT` | `/api/tickets/{id}/confirm` | Confirm an approved ticket. | Ticket ID | `TicketService` | `confirmTicket` |

## Endpoint rules

- Authentication and role authorization are enforced by the server.
- Request validation occurs before business-state changes.
- Success and error responses use the shared API envelope.
- Collection endpoints use bounded pagination where supported.

