# Tour Management

Core domain handling tours, transportation, tickets, seats, reservations, and meal plans.

## Entities
- **Tour** - Tour package with dates, pricing, capacity, and destinations
- **Transportation** - Vehicle/vessel (bus, flight, boat, train, etc.)
- **Seat** - Individual seat within a transportation unit
- **MealPlan** - Meal option available for tours
- **TourReservation** - Customer reservation for a tour
- **Ticket** - Individual passenger ticket with QR/barcode

## Services
- [TourService](services/TourService.md) - Tour lifecycle management
- [TransportationService](services/TransportationService.md) - Transport CRUD
- [SeatService](services/SeatService.md) - Seat management
- [MealPlanService](services/MealPlanService.md) - Meal plan management
- [TourReservationService](services/TourReservationService.md) - Reservation handling
- [TicketService](services/TicketService.md) - Ticket generation and management

## Endpoints
- [TourController](endpoints/TourController.md) - `/api/tours`
- [TransportationController](endpoints/TransportationController.md) - `/api/transportations`
- [SeatController](endpoints/SeatController.md) - `/api/seats`
- [MealPlanController](endpoints/MealPlanController.md) - `/api/meals`
- [TourReservationController](endpoints/TourReservationController.md) - `/api/reservations`
- [TicketController](endpoints/TicketController.md) - `/api/tickets`

## Business Logic
- Tours go through a workflow: PENDING -> APPROVED -> CONFIRMED -> COMPLETED/CANCELLED
- Auto-generated codes for tours, reservations, tickets, transport units
- Seat allocation prevents double-booking
- Reservations validate available capacity
- Tickets include QR codes and barcodes for verification
- Cancellation triggers refund calculation
- Scheduled tasks auto-complete expired tours and cancel unpaid reservations
