# Transportation Model

**Table:** `transportations`
**File:** `src/main/java/com/server/server/Models/tourmanagement/Transportation.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| transportationNumber | String | Unique, Generated | Auto-generated code |
| code | String | - | Short code |
| type | TransportationType | Not Null | BUS, FLIGHT, BOAT, TRAIN, PRIVATE_CAR, FERRY |
| providerName | String | - | Transport provider |
| status | TransportationStatus | Not Null | AVAILABLE, PARTIAL, FULL, MAINTENANCE, INACTIVE |
| totalCapacity | Integer | Not Null | Total seats |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| seats | Seat | OneToMany | Seat list |
| tours | Tour | OneToMany | Assigned tours |

## Computed Fields
- remainingSeats - Calculated from available seats
- calculatedAvailable - Real-time availability
