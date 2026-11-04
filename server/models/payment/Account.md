# Account

Table `accounts`. Inherits `BaseEntity`. Source: `models/payment/Account.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `accountNumber` | `String` |  unique, required |
| `accountName` | `String` |  required |
| `user` | `User` | OneToOne unique, required |
| `type` | `AccountType` |  required |
| `status` | `AccountStatus` |  required |
| `balance` | `BigDecimal` |  required |
| `version` | `Long` |   |
