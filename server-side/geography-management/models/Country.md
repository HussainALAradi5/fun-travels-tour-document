# Country Model

**Table:** `countries`
**File:** `src/main/java/com/server/server/Models/Country.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| famousName | String | - | Common name |
| officialName | String | Unique | Official country name |
| countryCode | String | - | ISO country code |
| flagPngUrl | String | - | PNG flag image URL |
| flagSvgUrl | String | - | SVG flag image URL |
