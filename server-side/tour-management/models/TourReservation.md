# TourReservation Model

**Table:** `tour_reservations`
**File:** `src/main/java/com/server/server/Models/tourmanagement/TourReservation.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| reservationNumber | String | Unique, Generated | Auto-generated code |
| requestedSlots | Integer | Not Null | Number of passengers |
| totalPrice | BigDecimal | Not Null | Total calculated price |
| status | GenericStatus | Not Null | PENDING, APPROVED, REJECTED, CONFIRMED, CANCELLED, COMPLETED |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| tour | Tour | ManyToOne | Reserved tour |
| user | User | ManyToOne | Customer |
| tickets | Ticket | OneToMany | Generated tickets |
| transactions | Transaction | OneToMany | Financial records |
| payments | Payment | OneToMany | Payment records |
