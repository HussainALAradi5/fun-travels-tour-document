# Tour Management (Client)

Core domain for tours, transportation, tickets, seats, meals, reservations, and booking.

## Components
- TourCreate, TourEdit, TourDetailsView, TourInventoryManager
- TransportationManager, TransportationCreate, TransportationTable
- TicketTable, CustomerTicketsManager, CustomerTicketDetailManager
- SeatManager, SeatPickerDialog, SeatEditDialog
- MealPlanManager, MealSelectionList, MealsSelectionDialog
- BookingManager, BookingCheckoutCard, BookingSummaryBar, GuestConfigCard
- CustomerTourCatalog, CustomerTourCatalogCard, CustomerTourCatalogTable

## Services
- [tourService](services/tourService.md)
- [transportationService](services/transportationService.md)
- [ticketService](services/ticketService.md)
- [seatService](services/seatService.md)
- [mealPlanService](services/mealPlanService.md)
- [reservationService](services/reservationService.md)

## Hooks
- [useTourManagement](hooks/useTourManagement.md) - Central tour CRUD hook

## Routes
| Route | Page | Access |
|-------|------|--------|
| /tours | CustomerCatalogPage | Public |
| /reserve/:tourId | BookingPage | Private |
| /my-bookings | CustomerTicketsPage | Private |
| /my-bookings/:id | CustomerTicketDetailPage | Private |
| /admin/tours | AdminToursPage | ADMIN |
| /admin/tours/create | TourCreatePage | ADMIN |
| /admin/tours/:id | AdminTourDetailsPage | ADMIN |
| /admin/transports | TransportPage | ADMIN |
| /admin/meals | MealsPage | ADMIN |
