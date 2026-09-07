# User Model

**Table:** `users`
**File:** `src/main/java/com/server/server/Models/User.java`

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK, Auto-generated | Unique identifier |
| userName | String | Unique, Not Blank | Login username |
| name | String | Not Blank | Display name |
| email | String | Unique, Not Blank | Email address |
| password | String | Not Blank | BCrypt hashed password |
| mobileNumber | String | Unique | Phone number |
| age | Integer | - | User age |
| userType | UserTypeEnum | Not Null | Role assignment |
| profileImageUrl | String | - | Profile image path |
| active | boolean | Default: true | Account active status |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| agency | Agency | ManyToOne | Employer agency |
| agencyBranch | AgencyBranch | ManyToOne | Assigned branch |
| account | Account | OneToOne | User wallet |

## Audit Fields
- createdAt, updatedAt (LocalDateTime)
- createdBy, updatedBy (User references)

## Enums
**UserTypeEnum:** ADMIN, MANAGER, EMPLOYEE, OWNER, CUSTOMER, SUPPORT_AGENT
