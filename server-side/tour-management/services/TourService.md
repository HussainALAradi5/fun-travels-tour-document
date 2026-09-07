# TourService

**File:** `src/main/java/com/server/server/services/tourmanagement/TourService.java`

Core tour lifecycle management.

## Methods

### getAllTours() -> List<Tour>
Returns all tours.

### getTourById(id) -> Tour
Returns tour by ID with all relationships.

### createTour(Tour) -> Tour
- Generates unique tourNumber
- Validates dates (start < end)
- Sets availableSlots = maxCapacity
- Sets initial status to PENDING

### updateTour(id, Tour) -> Tour
- Validates status allows editing
- Recalculates availableSlots if capacity changed

### updateStatus(id, GenericStatus) -> Tour
- Validates status transitions
- On APPROVED: sends notification to agency
- On CANCELLED: triggers refund logic
- On COMPLETED: marks all tickets as completed

### filterTours(FilterParams) -> Page<Tour>
Filters with pagination: status, agency, date range, price range, country

### getCatalog(FilterParams) -> Page<Tour>
Public catalog - only APPROVED future tours.

## Dependencies
- TourRepository, CodeGenerationService, NotificationService, GenericTrackingService
