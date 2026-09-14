# Tour Management

Tour management coordinates tours, transportation, seats, reservations, tickets, and meal plans as one operational workflow.

## Domain flow

1. An authorized agency user registers transportation and its seat layout.
2. A tour is configured with dates, destinations, capacity, meals, and optional transportation.
3. Workflow validation prevents invalid status changes and conflicting inventory usage.
4. A customer reservation holds capacity while checkout is completed.
5. Confirmed passengers receive tickets with seat, QR/barcode, and journey details.
6. Cancellation and completion update inventory and financial state consistently.

## Important rules

- Requested capacity cannot exceed available tour or transportation inventory.
- Seat allocation must not double-book a physical seat.
- Bulk seat layouts cannot exceed transportation capacity.
- Protected seat layouts cannot be changed while seats are unavailable or a linked tour is approved/active.
- Paginated list responses remain lightweight; detail queries explicitly load required relationships.
- Status transitions are validated centrally rather than accepted as arbitrary strings.

## Documentation

- [Tour service](services/TourService.md)
- [Transportation service](services/TransportationService.md)
- [Seat service](services/SeatService.md)
- [Reservation service](services/TourReservationService.md)
- [Inventory service](services/InventoryService.md)
- [Ticket service](services/TicketService.md)
- [Transportation endpoints](endpoints/TransportationController.md)
- [Seat endpoints](endpoints/SeatController.md)
