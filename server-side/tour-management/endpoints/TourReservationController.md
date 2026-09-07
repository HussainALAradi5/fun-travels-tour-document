# TourReservationController

**File:** `src/main/java/com/server/server/controllers/tourmanagement/TourReservationController.java`
**Base Path:** `/api/reservations`

## Endpoints

### POST /api/reservations

**Description:** Create a reservation
**Service Method:** `TourReservationService.create(res)`
**Request Body:** TourReservation entity
**Response (200 OK):** Created TourReservation entity
**Access:** Authenticated

---

### PATCH /api/reservations/{id}/status

**Description:** Update reservation status
**Service Method:** `TourReservationService.updateStatus(id, status)`
**Query Params:** status (GenericStatus)
**Response (200 OK):** Updated TourReservation entity
**Access:** Authenticated

---

### PATCH /api/reservations/{id}/cancel

**Description:** Cancel a reservation
**Service Method:** `TourReservationService.cancelReservation(id)`
**Response (200 OK):** Cancelled TourReservation entity
**Access:** CUSTOMER, ADMIN, MANAGER, EMPLOYEE

---

### GET /api/reservations/filter

**Description:** Filter reservations
**Service Method:** `TourReservationService.filter(status, customerId, agencyId)`
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| status | GenericStatus | No | Filter by status |
| customerId | Long | No | Filter by customer |
| agencyId | Long | No | Filter by agency |
**Response (200 OK):** List of TourReservation entities
**Access:** Authenticated

---

### GET /api/reservations

**Description:** Get all reservations
**Service Method:** `TourReservationService.getAll()`
**Response (200 OK):** List of TourReservation entities
**Access:** Authenticated

---

### GET /api/reservations/{id}

**Description:** Get reservation by ID
**Service Method:** `TourReservationService.getById(id)`
**Response (200 OK):** TourReservation entity
**Access:** Authenticated
