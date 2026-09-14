# Tour Management Client

The client module covers tour discovery, administration, booking, transportation, meals, seats, and tickets.

## Customer experience

- Search and filter available tours by route and date.
- Follow a step-by-step booking guide.
- Configure guests, seats, and meals.
- Review checkout totals before payment.
- View ticket status, boarding information, QR code, and ticket instructions.

## Operations experience

- Create and edit tours with optimized dynamic forms.
- Search agencies and branches through paginated backend selectors.
- Register transportation with visual vehicle-type icons.
- Import multiple transportation units through a generic Excel dialog.
- Generate specialized seats in bulk and manage individual seat details.
- Filter and sort tours, transportation, reservations, tickets, and seats.

## Important components

| Component | Responsibility |
|---|---|
| `CustomerTourCatalog` | Public tour discovery and filters |
| `BookingManager` | Guest and inventory selection |
| `CustomerTicketsManager` | Customer ticket history |
| `TransportationManager` | Fleet table and Excel import |
| `TransportationCreate` | Agency-aware unit registration and seat generation |
| `SeatManager` | Seat summary, filters, and editing workflow |
| `GuidedStepsDialog` | Reusable customer guidance |
