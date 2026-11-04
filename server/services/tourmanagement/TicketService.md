# TicketService

Source: `services/tourmanagement/TicketService.java`.

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

## Functions

### `void init()`

### `PageResponse<Ticket> getAll(Integer page, Integer size, String sortDir)`

**Runs in:** read-only transaction

### `Ticket getById(Integer id)`

**Runs in:** read-only transaction

### `Ticket updateStatus(Integer id, GenericStatus newStatus)`

**Purpose:** Staff progress a paid ticket: APPROVED, CONFIRMED, or COMPLETED. Cancellation has its own rules.

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

### `Ticket cancelTicket(Integer ticketId)`

**Purpose:** Cancels one ticket. A paid ticket is refunded by the notice-period policy; an unpaid one lowers the pending reservation total. The reservation is cancelled with its last ticket.

**Runs in:** transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER, CUSTOMER

### `Ticket create(TicketCreateRequest request)`

**Purpose:** Staff-issued walk-in ticket for an existing customer. It stays pending until paid.

**Runs in:** transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

### `PageResponse<Ticket> filter(TicketFilterRequest filter)`

**Runs in:** read-only transaction

### `void autoCancelExpiredTickets()`

**Purpose:** Nightly: unpaid tickets whose tour has started are cancelled and their places released.

**Runs in:** transaction
