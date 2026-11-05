# BookingLifecycleService

Source: `services/tourmanagement/BookingLifecycleService.java`.

Shared steps for every way a booking ends early: customer cancellation, hold expiry, staff rejection, and agency tour cancellation. Only tickets that are still active are released or refunded, so a ticket cancelled earlier is never refunded or freed twice.

## Business logic

Shared by customer cancellation, hold expiry, staff rejection, and agency tour cancellation, so all four end a booking the same way.

- `activeTickets` - tickets that are not CANCELLED.
- `activeTotal` - sum of active ticket prices; reservations created before tickets existed use their stored total.
- `releaseAndCancelTickets` - releases one place per active ticket (or `requestedSlots` for legacy reservations) and marks them cancelled with the given approval status.
- `refundToWallet` - credits the customer's wallet only for positive amounts.

| Case | Result |
| --- | --- |
| One of three tickets cancelled earlier, reservation then cancelled | Only the two active tickets are refunded and released |
| Legacy reservation without tickets | `requestedSlots` places released, stored total refunded |

## Functions

### `static List<Ticket> activeTickets(TourReservation reservation)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `static BigDecimal activeTotal(TourReservation reservation)`

**Purpose:** Amount still covered by the reservation; legacy reservations without tickets use their total.

**Exceptions:** none of its own; failures come from the functions it calls.

### `void releaseAndCancelTickets(TourReservation reservation, GenericStatus ticketApprovalStatus)`

**Purpose:** Returns held or sold places to inventory and marks the active tickets cancelled.

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.

### `void refundToWallet(TourReservation reservation, BigDecimal amount, TransactionType type, String reason)`

**Purpose:** Credits the customer's wallet when the amount is positive.

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.
