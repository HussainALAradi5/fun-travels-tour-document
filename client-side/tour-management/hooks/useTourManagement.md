# useTourManagement Hook

**File:** `src/hooks/tourManagement/useTourManagement.ts`

Central hook for all tour management operations (240 lines).

## Returns
```typescript
{
  tours: Tour[],
  loading: boolean,
  fetchTours, fetchTourById, createTour, updateTour, updateTourStatus, filterTours,
  transportations: Transportation[],
  createTransportation, updateTransportation,
  seats: Seat[],
  updateSeat, updateSeatStatus,
  tickets: Ticket[],
  createTicket, updateTicketStatus,
  reservations: TourReservation[],
  createReservation, cancelReservation,
  mealPlans: MealPlan[],
  createMealPlan, updateMealPlanStatus,
}
```
