# TicketService

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
