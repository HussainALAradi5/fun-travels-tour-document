# TourService

**File:** `src/main/java/com/server/server/services/tourmanagement/TourService.java`

## Methods

### create(Tour) -> Tour

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| tour | Tour | Tour entity with creation data |

**Returns:** Created Tour entity

**Business Logic:**
1. Gets current authenticated user
2. Multi-tenancy: auto-sets agency/branch from user context (EMPLOYEE, MANAGER, OWNER)
3. Resolves transportation by ID if provided
4. Validates tour dates (start not in past, end after start)
5. Calculates totalPrice = basePrice - discountPrice
6. Sets status to PENDING
7. Saves tour
8. Logs "CREATED" event via GenericTrackingService

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| WorkflowException | "Start date is required." |
| WorkflowException | "Start date cannot be in the past." |
| WorkflowException | "End date cannot be earlier than the start date." |

---

### updateTour(id, Tour) -> Tour

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Tour ID |
| tour | Tour | Tour entity with updated fields |

**Returns:** Updated Tour entity

**Business Logic:**
1. Fetches existing tour
2. Authorization check: only creator, branch manager, agency owner, or admin can edit
3. Cannot modify completed tours
4. Updates non-null fields (title, description, dates, capacity, price, locations, transport, meals)
5. Recalculates availableSlots if capacity changed
6. Recalculates totalPrice
7. Logs "UPDATED" event

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| WorkflowException | "Access Denied: You can only edit tours you created..." |
| WorkflowException | "Cannot modify a completed tour." |
| WorkflowException | Date validation errors |

---

### updateStatus(id, GenericStatus) -> Tour

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Tour ID |
| newStatus | GenericStatus | Target status |

**Returns:** Updated Tour entity

**Business Logic:**
1. Terminal state protection: cannot change completed tours
2. Cancellation recovery: cancelled tours can only go back to PENDING
3. Cancellation rules:
   - Must be at least 14 days away from start
   - Booked capacity must be <= 1/3 of max capacity
   - Wipes availableSlots to 0
4. Forward progression rules:
   - PENDING -> APPROVED or CANCELLED
   - APPROVED -> ACTIVE or CANCELLED
   - ACTIVE -> COMPLETED or CANCELLED
5. Initializes inventory when going ACTIVE (availableSlots = maxCapacity)

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| WorkflowException | "Cannot change the status of a completed tour." |
| WorkflowException | "A cancelled tour can only be restored to PENDING status." |
| WorkflowException | "Cancellation denied: Tour is less than 2 weeks away." |
| WorkflowException | "Cancellation denied: Booked seats exceed 1/3 of total capacity." |
| WorkflowException | "A pending tour must be APPROVED or CANCELLED." |

---

### getAll() -> List<Tour>

**Parameters:** None
**Returns:** List of all tours with details loaded

---

### getById(id) -> Tour

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| id | Integer | Tour ID |

**Returns:** Tour entity with all relationships

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| IllegalArgumentException | "Tour not found with id: {id}" |

---

### filter(status, minSlots, start, end, agencyId, branchId, minPrice, maxPrice, countryId, cityId, createdById, sortBy, sortDir) -> List<Tour>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| status | GenericStatus | Filter by status |
| minSlots | Integer | Minimum available slots |
| start | LocalDate | Start date range |
| end | LocalDate | End date range |
| agencyId | Long | Filter by agency |
| branchId | Long | Filter by branch |
| minPrice | Double | Minimum price |
| maxPrice | Double | Maximum price |
| countryId | Integer | Filter by country |
| cityId | Integer | Filter by city |
| createdById | Integer | Filter by creator |
| sortBy | String | Sort field |
| sortDir | String | Sort direction (asc/desc) |

**Returns:** Filtered list of tours

**Business Logic:**
1. Auto-applies agency/branch filter based on user role (EMPLOYEE/MANAGER/OWNER)
2. Uses JPA Specification for dynamic filtering
3. Supports sorting by any field

---

### restoreInventory(tourId, slotsToRestore) -> void

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| tourId | Integer | Tour ID |
| slotsToRestore | int | Slots to add/subtract (negative to decrease) |

**Business Logic:**
1. Fetches tour with pessimistic lock
2. Cannot modify completed tours
3. Adjusts availableSlots

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| WorkflowException | "Tour is completed. Inventory cannot be modified." |

---

### getCatalogTours(startCountryId, endCountryId, start, end) -> List<Tour>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| startCountryId | Integer | Filter by departure country |
| endCountryId | Integer | Filter by destination country |
| start | LocalDate | Filter by start date |
| end | LocalDate | Filter by end date |

**Returns:** List of approved tours for public catalog
