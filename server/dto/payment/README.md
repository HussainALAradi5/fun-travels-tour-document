# payment DTOs

Source: `dto/payment/`. Clients mirror these in `src/dtos/payment/`.

## AccountResponse

response record; built by `from(Account)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `accountNumber` | `String` | - |
| `accountName` | `String` | - |
| `balance` | `BigDecimal` | - |
| `type` | `String` | - |
| `status` | `String` | - |

## AccountSummary

response record; built by `from(Account)`. A wallet account by id, number, and name.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `accountNumber` | `String` | - |
| `accountName` | `String` | - |

## PaymentFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| (inherited) | `GenericFilterRequest` | `page`, `size`, `search`, `sortBy`, `sortDir` |
| `userId` | `Integer` | optional |
| `status` | `PaymentStatus` | optional |
| `method` | `PaymentMethod` | optional |
| `date` | `LocalDate` | optional |
| `startDate` | `LocalDate` | optional |
| `endDate` | `LocalDate` | optional |

## PaymentResponse

response record; built by `from(Payment)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `amount` | `BigDecimal` | - |
| `currency` | `String` | - |
| `method` | `PaymentMethod` | - |
| `status` | `PaymentStatus` | - |
| `transactionId` | `String` | - |
| `reservation` | `ReservationSummary` | - |
| `paymentDate` | `LocalDateTime` | - |

## TransactionFilterRequest

query parameters (class); built by bound from the query string.

| Field | Type | Rules |
| --- | --- | --- |
| (inherited) | `GenericFilterRequest` | `page`, `size`, `search`, `sortBy`, `sortDir` |
| `userId` | `Integer` | optional |
| `type` | `TransactionType` | optional |
| `startDate` | `LocalDate` | optional |
| `endDate` | `LocalDate` | optional |
| `agencyId` | `Long` | optional |
| `branchId` | `Long` | optional |

## TransactionResponse

response record; built by `from(Transaction)`.

| Field | Type | Rules |
| --- | --- | --- |
| `id` | `Integer` | - |
| `amount` | `BigDecimal` | - |
| `transactionType` | `TransactionType` | - |
| `description` | `String` | - |
| `account` | `AccountSummary` | - |
| `timestamp` | `LocalDateTime` | - |
