# AccountController

**File:** `src/main/java/com/server/server/controllers/Account/AccountController.java`
**Base Path:** `/api/accounts`

## Endpoints

### GET /api/accounts/user/{userId}/balance

**Description:** Get user account balance

**Service Method:** `AccountService.getAccountByUserId(userId)`

**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| userId | Integer | User ID |

**Response (200 OK):** Account entity with balance

**Access:** CUSTOMER, ADMIN, OWNER, MANAGER

---

### GET /api/accounts/user/{userId}/history

**Description:** Get user transaction history

**Service Method:** `AccountService.getAccountByUserId(userId)` + `AccountService.getTransactionHistory(accountId)`

**Path Params:**
| Param | Type | Description |
|-------|------|-------------|
| userId | Integer | User ID |

**Response (200 OK):** List of Transaction entities

**Access:** CUSTOMER, ADMIN
