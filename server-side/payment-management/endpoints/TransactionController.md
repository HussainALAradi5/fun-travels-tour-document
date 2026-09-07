# TransactionController

**File:** `src/main/java/com/server/server/controllers/TransactionController.java`
**Base Path:** `/api/transactions`

## Endpoints

### GET /api/transactions/filter

**Description:** Filter transactions
**Service Method:** `TransactionService.filterTransactions(...)`
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| userId | Integer | No | Filter by user |
| type | TransactionType | No | Filter by type |
| startDate | LocalDateTime | No | Start date |
| endDate | LocalDateTime | No | End date |
| agencyId | Long | No | Filter by agency |
| branchId | Long | No | Filter by branch |
| sortBy | String | No | Sort field (default: timestamp) |
| sortDir | String | No | Sort direction (default: desc) |
**Response (200 OK):** List of Transaction entities
**Access:** ADMIN, MANAGER, EMPLOYEE, CUSTOMER, OWNER

---

### POST /api/transactions/manual-credit/{userId}

**Description:** Manual wallet credit (admin only)
**Service Method:** `TransactionService.creditAccount(account, amount, MANUAL_ADJUSTMENT, description, null)`
**Path Params:** userId (Integer)
**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| amount | BigDecimal | Yes | Amount to credit |
| description | String | Yes | Credit description |
**Response (200 OK):** Transaction entity
**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Amount must be > 0, user not found |
**Access:** ADMIN
