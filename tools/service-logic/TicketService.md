## Business logic

### `cancelTicket(Integer ticketId)`

Customers cancel their own tickets; agency staff cancel tickets of their agency. A paid ticket is refunded by the notice-period policy (`PARTIAL_REFUND` transaction). One place is released and the seat becomes free for that tour. The parent reservation is then synchronized (see `TourReservationService.syncAfterTicketCancellation`).

| Case | Result |
| --- | --- |
| Already cancelled / completed | 409 |
| Tour completed | 409 |
| Another customer's ticket | 403 |

### `updateStatus(Integer id, GenericStatus newStatus)`

Owner, manager, or admin may move a **paid** ticket to APPROVED, CONFIRMED, or (after the tour completes) COMPLETED. Unpaid tickets cannot be approved (`TICKET_NOT_PAID`).

### `create(TicketCreateRequest request)`

Staff-issued walk-in ticket for an existing customer on a tour of the staff member's agency. It holds one place and stays PENDING and unpaid. Any client-sent reservation or price is ignored.

### `autoCancelExpiredTickets()`

Nightly: unpaid tickets of tours that have started are cancelled and their places released.
