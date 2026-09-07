# Agency Model

**Table:** `agencies`
**File:** `src/main/java/com/server/server/Models/Agency/Agency.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| agencyName | String | Not Blank | Agency name |
| address | String | - | Street address |
| contactNumber | String | - | Primary phone |
| ownerMobileNumber | String | - | Owner phone |
| active | boolean | Default: true | Active status |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| country | Country | ManyToOne | Country location |
| city | City | ManyToOne | City location |
| agencyOwner | User | ManyToOne | Owner user |
| branches | AgencyBranch | OneToMany | Agency branches |
| employees | User | OneToMany | Agency staff |
