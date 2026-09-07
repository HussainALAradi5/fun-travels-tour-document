# WalletController

**File:** `src/main/java/com/server/server/controllers/Account/WalletController.java`
**Base Path:** `/api/wallet`

## Endpoints

### GET /api/wallet/config

**Description:** Get Stripe publishable key for frontend

**Service Method:** `StripeConfig.getPublishableKey()`

**Response (200 OK):**
```json
{
  "publishableKey": "pk_test_xxx"
}
```

**Access:** Public

---

### POST /api/wallet/top-up

**Description:** Top up wallet balance via Stripe

**Service Method:** `WalletTopUpService.processWalletTopUp(amount, method, gatewayToken)`

**Query Params:**
| Param | Type | Required | Description |
|-------|------|----------|-------------|
| amount | BigDecimal | Yes | Amount to top up |
| method | PaymentMethod | Yes | Payment method (CREDIT_CARD, etc.) |
| gatewayToken | String | Yes | Stripe token from frontend |

**Response (200 OK):** Transaction entity

**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Amount must be greater than zero |
| 500 | Card Declined, Payment processing error |

**Access:** CUSTOMER, ADMIN, MANAGER, OWNER, EMPLOYEE
