# AccountService

**File:** `src/main/java/com/server/server/services/Account/AccountService.java`

## Code

```java
@Service
public class AccountService {
    @Autowired
    private AccountRepository accountRepository;
    @Autowired
    private TransactionRepository transactionRepository;
    @Autowired
    private UserRepository userRepository;

    @Transactional
    public Account createAccountForUser(User user) {
        if (accountRepository.findByUserId(user.getId()).isPresent()) {
            throw new RuntimeException("User already has an active account.");
        }
        Account account = new Account();
        account.setUser(user);
        account.setBalance(BigDecimal.ZERO);
        account.setAccountNumber("ACC-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase());
        account.setAccountName(user.getName() + "'s Digital Wallet");
        account.setType(AccountType.CUSTOMER_WALLET);
        account.setStatus(AccountStatus.ACTIVE);
        return accountRepository.save(account);
    }

    @Transactional
    public Account getAccountByUserId(Integer userId) {
        return accountRepository.findByUserId(userId)
                .orElseGet(() -> {
                    User user = userRepository.findById(userId)
                            .orElseThrow(() -> new RuntimeException("User not found"));
                    return createAccountForUser(user);
                });
    }

    public List<Transaction> getTransactionHistory(Integer accountId) {
        return transactionRepository.findByAccountIdOrderByTimestampDesc(accountId);
    }
}
```

## Methods

### createAccountForUser(User) -> Account

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| user | User | User entity to create account for |

**Returns:** Created Account entity

**Business Logic:**
1. Checks if user already has an account (throws if exists)
2. Creates new Account with zero balance
3. Generates account number: "ACC-" + random 8 chars
4. Sets account name: "{user name}'s Digital Wallet"
5. Sets type to CUSTOMER_WALLET
6. Sets status to ACTIVE
7. Saves to database

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "User already has an active account." |

---

### getAccountByUserId(userId) -> Account

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| userId | Integer | User ID |

**Returns:** Account entity (creates one if missing - auto-heal)

**Business Logic:**
1. Looks up account by user ID
2. If not found, fetches the user and auto-creates an account
3. This is an "auto-heal" pattern ensuring every user always has an account

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| RuntimeException | "User not found" (only if user doesn't exist) |

---

### getTransactionHistory(accountId) -> List<Transaction>

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| accountId | Integer | Account ID |

**Returns:** List of transactions sorted by timestamp descending
