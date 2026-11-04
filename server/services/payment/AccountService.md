# AccountService

Source: `services/payment/AccountService.java`.

## Functions

### `Account createAccountForUser(User user)`

**Runs in:** transaction

### `Account getAccountByUserId(Integer userId)`

**Runs in:** transaction

### `Account getAccountForViewer(Integer userId)`

**Purpose:** Wallet of a user, visible to that user and to administrators.

**Runs in:** transaction

### `List<Transaction> getTransactionHistory(Integer accountId)`

**Runs in:** read-only transaction
