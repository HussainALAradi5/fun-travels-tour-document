# TicketIssuingService

Source: `services/tourmanagement/TicketIssuingService.java`.

Builds priced tickets with numbers and scan codes. Prices always come from the stored tour, seat, and meal records, never from the request.

## Business logic

- `issue` builds one unsaved ticket per traveler selection with a `TKT-` number, QR code (`TICKET|TOUR|CUSTOMER` payload), and Code 128 barcode.
- Meals must be offered by the tour, ACTIVE, and not selected twice for the same traveler.
- `applyPricing` = (tour price - 50% kids-chair discount) + seat price modifier + selected meal prices, never below zero (`PricingCalculator.ticketPrice`). It runs again after seats are auto-assigned so the assigned seat's modifier and discount apply.

## Functions

### `List<Ticket> issue(Tour tour, User customer, TourReservation reservation, List<TicketSelectionRequest> selections)`

**Purpose:** Creates one unsaved ticket per traveler selection.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Meal ' ' was selected twice. | `WorkflowException` | 409 |
| Meal ' ' is no longer available. | `WorkflowException` | 409 |
| Meal ' ' is not offered on this tour. | `WorkflowException` | 409 |
| Ticket codes could not be generated. | `WorkflowException` | 409 |

### `Ticket prepare(Ticket ticket, Tour tour, User customer, TourReservation reservation)`

**Purpose:** Fills identity, codes, relations, and price on a ticket.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Ticket codes could not be generated. | `WorkflowException` | 409 |

### `void applyPricing(Ticket ticket, Tour tour)`

**Purpose:** Recalculates price from the stored tour, seat, and meals.

**Exceptions:** none of its own; failures come from the functions it calls.
