# AccountService

Source: `services/payment/AccountService.java`.

## Functions

### `Account createAccountForUser(User user)`

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| User already has an active account. | `DuplicateResourceException` | 409 |

### `Account getAccountByUserId(Integer userId)`

**Purpose:** The user's wallet, created on first use for accounts that predate wallets.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| User not found | `ResourceNotFoundException` | 404 |
| User already has an active account. | `DuplicateResourceException` | 409 |

### `Account getAccountForViewer(Integer userId)`

**Purpose:** Wallet of a user, visible to that user and to administrators.

**Runs in:** transaction

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Caller lacks the role, ownership, or agency access | `AccessDeniedException` | 403 |
| User not found | `ResourceNotFoundException` | 404 |
| User already has an active account. | `DuplicateResourceException` | 409 |

### `List<Transaction> getTransactionHistory(Integer accountId)`

**Runs in:** read-only transaction

**Exceptions:** none of its own; failures come from the functions it calls.
