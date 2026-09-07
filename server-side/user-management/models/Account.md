# Account Model

**Table:** `accounts`
**File:** `src/main/java/com/server/server/Models/Account.java`

Wallet/account entity for financial operations.

## Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK | Unique identifier |
| accountType | AccountType | Not Null | CUSTOMER_WALLET, AGENCY_WALLET, SYSTEM_WALLET |
| balance | BigDecimal | Default: 0 | Current balance |
| status | AccountStatus | Not Null | ACTIVE, FROZEN, CLOSED |

## Relationships

| Relation | Target | Type | Description |
|----------|--------|------|-------------|
| user | User | OneToOne | Account owner |

## Enums
**AccountType:** CUSTOMER_WALLET, AGENCY_WALLET, SYSTEM_WALLET
**AccountStatus:** ACTIVE, FROZEN, CLOSED
