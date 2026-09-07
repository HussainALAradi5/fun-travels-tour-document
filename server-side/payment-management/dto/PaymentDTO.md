# Payment & Transaction DTOs

## PaymentResponse

```java
public class PaymentResponse {
    private Integer id;
    private BigDecimal amount;
    private String currency;
    private PaymentMethod method;
    private PaymentStatus status;
    private String transactionId;
    private ReservationSummary reservation;
    private LocalDateTime paymentDate;
}
```

## PaymentFilterParams

```java
public class PaymentFilterParams {
    private Integer userId;
    private PaymentStatus status;
    private PaymentMethod method;
    private LocalDate date;
}
```

## TransactionResponse

```java
public class TransactionResponse {
    private Integer id;
    private BigDecimal amount;
    private TransactionType transactionType;
    private String description;
    private AccountSummary account;
    private PaymentSummary payment;
    private ReservationSummary reservation;
    private LocalDateTime timestamp;
}
```

## TransactionFilterParams

```java
public class TransactionFilterParams {
    private Integer userId;
    private TransactionType type;
    private LocalDateTime startDate;
    private LocalDateTime endDate;
    private Long agencyId;
    private Long branchId;
    private String sortBy;
    private String sortDir;
}
```

## WalletTopUpRequest

```java
public class WalletTopUpRequest {
    private BigDecimal amount;
    private PaymentMethod method;
    private String gatewayToken; // Stripe token
}
```

## ManualCreditRequest

```java
public class ManualCreditRequest {
    private Integer userId;
    private BigDecimal amount;
    private String description;
}
```
