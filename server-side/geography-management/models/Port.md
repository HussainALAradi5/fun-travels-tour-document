# Port Model

**Table:** `ports`
**File:** `src/main/java/com/server/server/Models/Port.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| name | String | Not Blank | Port name |
| portType | PortType | Not Null | AIRPORT, SEAPORT, TRAIN_STATION, BUS_TERMINAL, HELIPORT, LANDING_ZONE |
| active | boolean | Default: true | Active status |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| city | City | ManyToOne | City location |
| country | Country | ManyToOne | Country location |
