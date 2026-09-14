# TicketService

## Additional public function reference

| Function and signature | Parameters | Logic and business purpose | Return / side effects | Exceptions |
|---|---|---|---|---|
| `public Ticket cancelTicket(Integer ticketId)` | Required ticket ID | Validates ownership/state/tour timing, applies refund rules where eligible, releases inventory, cancels, saves, and notifies. | Cancelled ticket plus inventory/financial/notification writes. | `"You are not authorized to cancel this ticket."`, `"Ticket is already cancelled."`, `"Cannot cancel a ticket for a completed tour."` |
| `public Ticket approveTicket(Integer id)` | Ticket ID | Delegates to the approved workflow transition. | Approved ticket. | Paid-reservation and transition failures propagate. |
| `public Ticket confirmTicket(Integer id)` | Ticket ID | Delegates to the confirmed workflow transition. | Confirmed ticket. | Workflow transition failures propagate. |
| `public void autoCancelExpiredTickets()` | None | Finds pending tickets for past tours, cancels them, releases inventory, saves, notifies, and isolates/logs each failure. | Batch state changes and notifications. | Per-ticket exceptions are caught and logged. |

**File:** `src/main/java/com/server/server/services/tourmanagement/TicketService.java`

## Methods

### getAll() -> List<Ticket>
### getById(id) -> Ticket

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| IllegalArgumentException | "Ticket not found with id: {id}" |

---

### create(Ticket) -> Ticket

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| ticket | Ticket | Ticket entity |

**Returns:** Created Ticket entity

**Business Logic:**
1. Sets initial ticketStatus to PENDING
2. Generates ticket number
3. Saves ticket

---

### updateStatus(id, GenericStatus) -> Ticket

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Ticket ID |
| status | GenericStatus | New status |

**Returns:** Updated Ticket entity

**Business Logic:**
- APPROVED: marks ticket as approved
- CONFIRMED: confirms ticket
- CANCELLED: cancels ticket, restores seat availability

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| WorkflowException | Invalid status transition |

---

### filter(status, customerId, tourId, sortBy, sortDir) -> List<Ticket>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| status | TicketStatus | Filter by status |
| customerId | Long | Filter by customer |
| tourId | Integer | Filter by tour |
| sortBy | String | Sort field |
| sortDir | String | Sort direction |

**Returns:** Filtered list of tickets
