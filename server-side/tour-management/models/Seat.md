# Seat Model

**Table:** `seats`
**File:** `src/main/java/com/server/server/Models/tourmanagement/Seat.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| seatCode | String | Not Blank | Seat identifier (e.g., "A1", "B2") |
| chairType | ChairType | Not Null | STANDARD, KIDS_CHAIR, WHEELCHAIR_ACCESSIBLE, PREMIUM_RECLINER |
| status | SeatStatus | Not Null | AVAILABLE, BOOKED, RESERVED, MAINTENANCE |
| seatPriceModifier | BigDecimal | Default: 0 | Price adjustment for this seat |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| transportation | Transportation | ManyToOne | Parent transport |
