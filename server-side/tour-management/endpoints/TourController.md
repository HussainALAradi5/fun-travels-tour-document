# TourController

**File:** `src/main/java/com/server/server/controllers/tourmanagement/TourController.java`
**Base Path:** `/api/tours`

## Endpoints

### GET /api/tours
Get all tours.
**Access:** ADMIN, MANAGER, EMPLOYEE, OWNER

### GET /api/tours/{id}
Get tour by ID.
**Access:** ADMIN, MANAGER, EMPLOYEE, OWNER

### POST /api/tours
Create a new tour.
**Access:** ADMIN, MANAGER, OWNER

### PUT /api/tours/{id}
Update tour details.
**Access:** ADMIN, MANAGER, OWNER

### PATCH /api/tours/{id}/status
Update tour status.
**Access:** ADMIN, MANAGER, OWNER

### GET /api/tours/filter
Filter tours with pagination.
**Access:** ADMIN, MANAGER, EMPLOYEE, OWNER

### GET /api/tours/catalog
Public tour catalog.
**Access:** Public
