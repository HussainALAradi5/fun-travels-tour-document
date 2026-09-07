# GenericComment Model

**Table:** `generic_comments`
**File:** `src/main/java/com/server/server/Models/GenericComment.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| referenceType | String | Not Blank | Entity type name |
| referenceId | Long | Not Null | Entity ID |
| content | String | Not Blank | Comment text |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| author | User | ManyToOne | Comment author |
| updatedBy | User | ManyToOne | Last editor |
