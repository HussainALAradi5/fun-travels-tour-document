# Tour Management DTOs

## TourCreateRequest

```java
public class TourCreateRequest {
    private String title;
    private String description;
    private Double basePrice;
    private Integer numberOfDays;
    private LocalDate startDate;
    private LocalDate endDate;
    private Integer maxCapacity;
    private Integer startCountryId;
    private Integer endCountryId;
    private Integer startCityId;
    private Integer endCityId;
    private List<Integer> destinationCountryIds;
    private Integer transportationId;
    private List<Integer> mealPlanIds;
}
```

## TourUpdateRequest

```java
public class TourUpdateRequest {
    private String title;
    private String description;
    private Double basePrice;
    private Integer numberOfDays;
    private LocalDate startDate;
    private LocalDate endDate;
    private Integer maxCapacity;
    private Integer startCountryId;
    private Integer endCountryId;
    private Integer startCityId;
    private Integer endCityId;
    private List<Integer> destinationCountryIds;
    private Integer transportationId;
    private List<Integer> mealPlanIds;
}
```

## TourResponse

```java
public class TourResponse {
    private Integer id;
    private String tourNumber;
    private String title;
    private String description;
    private Double basePrice;
    private Double discountPrice;
    private Double totalPrice;
    private Integer numberOfDays;
    private LocalDate startDate;
    private LocalDate endDate;
    private Integer maxCapacity;
    private Integer availableSlots;
    private GenericStatus status;
    private CountrySummary startCountry;
    private CountrySummary endCountry;
    private CitySummary startCity;
    private CitySummary endCity;
    private List<CountrySummary> destinationCountries;
    private AgencySummary agency;
    private AgencyBranchSummary agencyBranch;
    private TransportationSummary transportation;
    private List<MealPlanSummary> availableMeals;
    private UserSummary createdBy;
    private LocalDateTime createdAt;
}
```

## TourStatusUpdateRequest

```java
public class TourStatusUpdateRequest {
    private GenericStatus status;
}
```

## TourFilterParams

```java
public class TourFilterParams {
    private GenericStatus status;
    private Integer minSlots;
    private LocalDate startDate;
    private LocalDate endDate;
    private Long agencyId;
    private Long branchId;
    private Double minPrice;
    private Double maxPrice;
    private Integer countryId;
    private Integer cityId;
    private Integer createdById;
    private String sortBy;
    private String sortDir;
}
```

## TicketCreateRequest

```java
public class TicketCreateRequest {
    private Integer tourId;
    private Integer customerId;
    private Integer seatId;
    private Integer transportationId;
    private Integer destinationCityId;
    private Integer guestCount;
    private BigDecimal unitPrice;
    private BigDecimal discountAmount;
    private LocalDate bookingDate;
    private boolean hasMealPlan;
    private List<Integer> selectedMealIds;
}
```

## TicketResponse

```java
public class TicketResponse {
    private Integer id;
    private String ticketNumber;
    private UserSummary customer;
    private TourSummary tour;
    private SeatSummary assignedSeat;
    private TransportationSummary transportation;
    private CitySummary destinationCity;
    private Integer guestCount;
    private BigDecimal unitPrice;
    private BigDecimal totalPrice;
    private BigDecimal discountAmount;
    private LocalDate bookingDate;
    private boolean paid;
    private TicketStatus ticketStatus;
    private GenericStatus approvalStatus;
    private boolean hasMealPlan;
    private List<MealPlanSummary> selectedMeals;
    private LocalDateTime createdAt;
}
```

## ReservationCreateRequest

```java
public class ReservationCreateRequest {
    private Integer tourId;
    private Integer userId;
    private Integer requestedSlots;
}
```

## ReservationResponse

```java
public class ReservationResponse {
    private Integer id;
    private String reservationNumber;
    private TourSummary tour;
    private UserSummary user;
    private Integer requestedSlots;
    private BigDecimal totalPrice;
    private GenericStatus status;
    private List<TicketSummary> tickets;
    private LocalDateTime createdAt;
}
```

## TransportationCreateRequest

```java
public class TransportationCreateRequest {
    private TransportationType type;
    private String providerName;
    private Integer totalCapacity;
    private List<SeatConfig> seats;
}

public class SeatConfig {
    private String seatCode;
    private ChairType chairType;
    private BigDecimal seatPriceModifier;
}
```

## TransportationResponse

```java
public class TransportationResponse {
    private Integer id;
    private String transportationNumber;
    private String code;
    private TransportationType type;
    private String providerName;
    private TransportationStatus status;
    private GenericStatus unitStatus;
    private Integer totalCapacity;
    private Integer remainingSeats;
    private Integer calculatedAvailable;
    private List<SeatSummary> seats;
}
```

## SeatResponse

```java
public class SeatResponse {
    private Integer id;
    private String seatCode;
    private ChairType chairType;
    private SeatStatus status;
    private BigDecimal seatPriceModifier;
}
```

## MealPlanCreateRequest

```java
public class MealPlanCreateRequest {
    private String mealName;
    private BigDecimal mealPrice;
    private String mealDescription;
    private boolean isVegetarian;
    private boolean isVegan;
    private boolean isGlutenFree;
}
```

## MealPlanResponse

```java
public class MealPlanResponse {
    private Integer id;
    private String mealName;
    private BigDecimal mealPrice;
    private String mealDescription;
    private boolean isVegetarian;
    private boolean isVegan;
    private boolean isGlutenFree;
    private GenericStatus status;
}
```
