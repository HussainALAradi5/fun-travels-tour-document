# City Model

**Table:** `cities`
**File:** `src/main/java/com/server/server/Models/City.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| name | String | Not Blank | City name |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| country | Country | ManyToOne | Parent country |
