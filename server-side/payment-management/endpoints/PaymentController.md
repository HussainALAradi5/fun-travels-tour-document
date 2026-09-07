# PaymentController

**File:** `src/main/java/com/server/server/controllers/PaymentController.java`
**Base Path:** `/api/payments`

## Endpoints

### POST /api/payments/execute/{reservationId}

**Description:** Execute payment for a reservation
**Service Method:** `TourReservationService.finalizeReservationWithPayment(reservationId, method)`
**Path Params:** reservationId (Integer)
**Query Params:** method (PaymentMethod)
**Response (200 OK):** Updated TourReservation
**Access:** CUSTOMER, ADMIN, MANAGER

---

### GET /api/payments/filter

**Description:** Filter payments
**Service Method:** `PaymentService.filter(userId, status, method, date)`
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| userId | Integer | No | Filter by user |
| status | PaymentStatus | No | Filter by status |
| method | PaymentMethod | No | Filter by method |
| date | LocalDate | No | Filter by date |
**Response (200 OK):** List of Payment entities
**Access:** CUSTOMER, ADMIN, MANAGER
