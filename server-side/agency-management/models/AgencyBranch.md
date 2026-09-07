# AgencyBranch Model

**Table:** `agency_branch`
**File:** `src/main/java/com/server/server/Models/Agency/AgencyBranch.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| branchName | String | Not Blank | Branch name |
| branchAddress | String | - | Branch address |
| contactNumber | String | - | Branch phone |
| ownerMobileNumber | String | - | Manager phone |
| active | boolean | Default: true | Active status |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| agency | Agency | ManyToOne | Parent agency |
| country | Country | ManyToOne | Country |
| city | City | ManyToOne | City |
| branchManager | User | ManyToOne | Branch manager |
