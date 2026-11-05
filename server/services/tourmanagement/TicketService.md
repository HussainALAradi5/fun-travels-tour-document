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

**Exceptions:** none of its own; failures come from the functions it calls.

### `PageResponse<Ticket> getAll(Integer page, Integer size, String sortDir)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `Ticket getById(Integer id)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Ticket not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `RefundQuoteResponse refundQuote(Integer id)`

**Purpose:** What cancelling this ticket now would refund; nothing for an unpaid or cancelled ticket.

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Ticket not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `Ticket updateStatus(Integer id, GenericStatus newStatus)`

**Purpose:** Staff progress a paid ticket: APPROVED, CONFIRMED, or COMPLETED. Cancellation has its own rules.

**Runs in:** transaction; roles: ADMIN, MANAGER, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| A cancelled or completed ticket cannot change status. | `WorkflowException` | 409 |
| Ticket status can only progress to APPROVED, CONFIRMED, or COMPLETED. | `WorkflowException` | 409 |
| Cannot approve this ticket before it is paid. | `WorkflowException` | 409 |
| A ticket can only be completed after the tour is completed. | `WorkflowException` | 409 |
| Ticket not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| Ticket is already cancelled. | `WorkflowException` | 409 |
| A completed ticket cannot be cancelled. | `WorkflowException` | 409 |
| Cannot cancel a ticket for a completed tour. | `WorkflowException` | 409 |

### `Ticket cancelTicket(Integer ticketId)`

**Purpose:** Cancels one ticket. A paid ticket is refunded by the notice-period policy; an unpaid one lowers the pending reservation total. The reservation is cancelled with its last ticket.

**Runs in:** transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER, CUSTOMER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Ticket is already cancelled. | `WorkflowException` | 409 |
| A completed ticket cannot be cancelled. | `WorkflowException` | 409 |
| Cannot cancel a ticket for a completed tour. | `WorkflowException` | 409 |
| Ticket not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `Ticket create(TicketCreateRequest request)`

**Purpose:** Staff-issued walk-in ticket for an existing customer. It stays pending until paid.

**Runs in:** transaction; roles: ADMIN, MANAGER, EMPLOYEE, OWNER

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| User not found | `ResourceNotFoundException` | 404 |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `PageResponse<Ticket> filter(TicketFilterRequest filter)`

**Runs in:** read-only transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |

### `void autoCancelExpiredTickets()`

**Purpose:** Nightly: unpaid tickets whose tour has started are cancelled and their places released.

**Runs in:** transaction

**Exceptions:** none of its own; failures come from the functions it calls.
