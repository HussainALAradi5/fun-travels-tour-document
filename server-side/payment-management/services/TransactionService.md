# TransactionService

**File:** `src/main/java/com/server/server/services/TransactionService.java`

## Methods

### creditAccount(Account, BigDecimal, TransactionType, String, TourReservation) -> Transaction

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| account | Account | Account to credit |
| amount | BigDecimal | Amount to add |
| type | TransactionType | Transaction type |
| description | String | Transaction description |
| reservation | TourReservation | Optional linked reservation |

**Returns:** Created Transaction entity

**Business Logic:**
1. Adds amount to account balance
2. Creates Transaction record
3. Saves both to database

---

### debitAccount(Account, BigDecimal, TransactionType, String, TourReservation) -> Transaction

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| account | Account | Account to debit |
| amount | BigDecimal | Amount to deduct |
| type | TransactionType | Transaction type |
| description | String | Transaction description |
| reservation | TourReservation | Optional linked reservation |

**Returns:** Created Transaction entity

**Business Logic:**
1. Validates sufficient balance
2. Deducts amount from account balance
3. Creates Transaction record
4. Saves both to database

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "Insufficient balance" |

---

### filterTransactions(userId, type, startDate, endDate, agencyId, branchId, sortBy, sortDir) -> List<Transaction>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| userId | Integer | Filter by user |
| type | TransactionType | Filter by type |
| startDate | LocalDateTime | Start date range |
| endDate | LocalDateTime | End date range |
| agencyId | Long | Filter by agency |
| branchId | Long | Filter by branch |
| sortBy | String | Sort field |
| sortDir | String | Sort direction |

**Returns:** Filtered list of transactions
