# AccountService

**File:** `src/main/java/com/server/server/services/Account/AccountService.java`

Wallet/account management.

## Methods

### getBalance(userId) -> BigDecimal
Get account balance for a user.

### getAccountHistory(userId) -> List<Transaction>
Get transaction history for a user.

### createAccount(User, AccountType) -> Account
Create new account (called during registration).

### freezeAccount(accountId) -> Account
Freeze account (prevents transactions).

### closeAccount(accountId) -> Account
Close account permanently.

## Dependencies
- AccountRepository
- TransactionRepository
