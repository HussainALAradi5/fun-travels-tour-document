# PaymentController

**File:** `src/main/java/com/server/server/controllers/PaymentController.java`
**Base Path:** `/api/payments`

## Endpoints

### POST /api/payments/execute
Execute payment for reservation.
**Access:** CUSTOMER, ADMIN, MANAGER

### GET /api/payments/filter
Filter payments with pagination.
**Access:** ADMIN, MANAGER

### GET /api/payments/{id}
Get payment by ID.
**Access:** ADMIN, MANAGER, CUSTOMER (own)
