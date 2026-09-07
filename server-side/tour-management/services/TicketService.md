# TicketService

**File:** `src/main/java/com/server/server/services/tourmanagement/TicketService.java`

## Methods

### getAll() -> List<Ticket>
### getById(id) -> Ticket
### create(Ticket) -> Ticket
### updateStatus(id, status) -> Ticket
### approve(id) -> Ticket
### confirm(id) -> Ticket
### cancel(id) -> Ticket
Triggers refund logic.

### filter(FilterParams) -> Page<Ticket>
