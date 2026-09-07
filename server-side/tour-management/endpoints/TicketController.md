# TicketController

**File:** `src/main/java/com/server/server/controllers/tourmanagement/TicketController.java`
**Base Path:** `/api/tickets`

## Endpoints

### GET /api/tickets/filter

**Description:** Filter tickets
**Service Method:** `TicketService.filter(status, customerId, tourId, sortBy, sortDir)`
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| status | TicketStatus | No | Filter by status |
| customerId | Long | No | Filter by customer |
| tourId | Integer | No | Filter by tour |
| sortBy | String | No | Sort field |
| sortDir | String | No | Sort direction |
**Response (200 OK):** List of Ticket entities
**Access:** Authenticated

---

### GET /api/tickets

**Description:** Get all tickets
**Service Method:** `TicketService.getAll()`
**Response (200 OK):** List of Ticket entities
**Access:** Authenticated

---

### GET /api/tickets/{id}

**Description:** Get ticket by ID
**Service Method:** `TicketService.getById(id)`
**Path Params:** id (Integer) - Ticket ID
**Response (200 OK):** Ticket entity
**Access:** Authenticated

---

### POST /api/tickets

**Description:** Create a ticket
**Service Method:** `TicketService.create(ticket)`
**Request Body:** Ticket entity
**Response (200 OK):** Created Ticket entity
**Access:** Authenticated

---

### PUT /api/tickets/{id}/status

**Description:** Update ticket status
**Service Method:** `TicketService.updateStatus(id, status)`
**Query Params:** status (GenericStatus)
**Response (200 OK):** Updated Ticket entity
**Access:** Authenticated

---

### PUT /api/tickets/{id}/cancel

**Description:** Cancel a ticket
**Service Method:** `TicketService.updateStatus(id, CANCELLED)`
**Response (200 OK):** Cancelled Ticket entity
**Access:** Authenticated

---

### PUT /api/tickets/{id}/approve

**Description:** Approve a ticket
**Service Method:** `TicketService.updateStatus(id, APPROVED)`
**Response (200 OK):** Approved Ticket entity
**Access:** Authenticated

---

### PUT /api/tickets/{id}/confirm

**Description:** Confirm a ticket
**Service Method:** `TicketService.updateStatus(id, CONFIRMED)`
**Response (200 OK):** Confirmed Ticket entity
**Access:** Authenticated
