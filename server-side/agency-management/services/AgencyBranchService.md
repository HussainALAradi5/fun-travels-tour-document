# AgencyBranchService

**File:** `src/main/java/com/server/server/services/agency/AgencyBranchService.java`

## Methods

### getAllBranches() -> List<AgencyBranch>

**Parameters:** None
**Returns:** List of all branches
**Exceptions:** None

---

### getBranchesByAgency(agencyId) -> List<AgencyBranch>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| agencyId | Integer | Agency ID |

**Returns:** List of active branches for agency
**Exceptions:** None

---

### addBranch(agencyId, AgencyBranch) -> AgencyBranch

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| agencyId | Integer | Parent agency ID |
| branch | AgencyBranch | Branch entity with branchName, branchAddress, contactNumber |

**Returns:** Created AgencyBranch entity

**Business Logic:**
1. Validates agency exists
2. Checks branch name uniqueness within agency (case-insensitive)
3. Sets agency relationship
4. Saves branch
5. If branch manager specified, fetches user and links to agency/branch

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Agency not found with id: {id}" |
| RuntimeException | "A branch named '{name}' already exists for {agency}" |
| RuntimeException | "User assigned as Manager not found." |

---

### getEmployeesByBranch(agencyId, branchId) -> List<User>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| agencyId | Integer | Agency ID (security check) |
| branchId | Integer | Branch ID |

**Returns:** List of EMPLOYEE users in branch

**Business Logic:**
1. Fetches branch by ID
2. Validates branch belongs to specified agency (security check)
3. Returns employees with EMPLOYEE type

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Branch not found" |
| RuntimeException | "Security Alert: This branch does not belong to the specified agency." |
