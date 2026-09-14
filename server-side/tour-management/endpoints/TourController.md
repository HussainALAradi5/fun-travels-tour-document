# TourController

**File:** `src/main/java/com/server/server/controllers/tourmanagement/TourController.java`
**Base Path:** `/api/tours`

## Endpoints

### GET /api/tours/catalog

**Description:** Public tour catalog (approved tours only)
**Service Method:** `TourService.getCatalogTours(startCountryId, endCountryId, startDate, endDate)`
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| startCountryId | Integer | No | Departure country |
| endCountryId | Integer | No | Destination country |
| startDate | LocalDate | No | Start date filter |
| endDate | LocalDate | No | End date filter |
**Response (200 OK):** List of Tour entities
**Access:** Public

---

### GET /api/tours/search

**Description:** Filter tours with pagination and sorting
**Service Method:** `TourService.filter(...)`
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| status | GenericStatus | No | Filter by status |
| minSlots | Integer | No | Minimum available slots |
| startDate | LocalDate | No | Start date |
| endDate | LocalDate | No | End date |
| agencyId | Long | No | Agency ID |
| branchId | Long | No | Branch ID |
| minPrice | Double | No | Minimum price |
| maxPrice | Double | No | Maximum price |
| countryId | Integer | No | Country ID |
| cityId | Integer | No | City ID |
| createdById | Integer | No | Creator user ID |
| sortBy | String | No | Sort field |
| sortDir | String | No | asc/desc |
**Response (200 OK):** `ApiResponse<PageResponse<TourResponse>>`
**Access:** ADMIN, MANAGER, EMPLOYEE, OWNER

---

### GET /api/tours

**Description:** Get all tours
**Service Method:** `TourService.getAll()`
**Response (200 OK):** `ApiResponse<PageResponse<TourResponse>>`
**Access:** ADMIN, MANAGER, EMPLOYEE, OWNER

---

### GET /api/tours/{id}

**Description:** Get tour by ID
**Service Method:** `TourService.getById(id)`
**Path Params:** id (Integer) - Tour ID
**Response (200 OK):** Tour entity
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | "Tour not found with id: {id}" |
**Access:** ADMIN, MANAGER, EMPLOYEE, OWNER

---

### POST /api/tours

**Description:** Create a new tour
**Service Method:** `TourService.create(tour)`
**Request Body:**
```json
{
  "title": "string",
  "description": "string",
  "basePrice": 999.99,
  "numberOfDays": 7,
  "startDate": "2026-10-01",
  "endDate": "2026-10-07",
  "maxCapacity": 50,
  "startCountry": { "id": 1 },
  "endCountry": { "id": 2 },
  "startCity": { "id": 1 },
  "endCity": { "id": 2 },
  "destinationCountries": [{ "id": 2 }, { "id": 3 }],
  "transportation": { "id": 1 },
  "availableMeals": [{ "id": 1 }]
}
```
**Response (200 OK):** Created Tour entity
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Date validation errors |
| 403 | Access denied |
**Access:** ADMIN, MANAGER, EMPLOYEE, OWNER

---

### PUT /api/tours/{id}

**Description:** Update tour details
**Service Method:** `TourService.updateTour(id, tour)`
**Path Params:** id (Integer) - Tour ID
**Request Body:** Tour entity with updated fields
**Response (200 OK):** Updated Tour entity
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Access denied, completed tour, date validation |
**Access:** ADMIN, MANAGER, EMPLOYEE, OWNER

---

### PUT /api/tours/{id}/status

**Description:** Update tour status (workflow transition)
**Service Method:** `TourService.updateStatus(id, status)`
**Path Params:** id (Integer) - Tour ID
**Query Params:** status (GenericStatus) - Target status
**Response (200 OK):** Updated Tour entity
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Invalid transition, cancellation rules violated |
**Access:** ADMIN, MANAGER, EMPLOYEE
