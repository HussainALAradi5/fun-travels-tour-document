# Enums

| Domain | Enum | Values |
| --- | --- | --- |
| common | `GenericStatus` | `PENDING`, `APPROVED`, `REJECTED`, `CONFIRMED`, `CANCELLED`, `COMPLETED`, `ACTIVE`, `INACTIVE` |
| geography | `PortType` | `AIRPORT`, `SEAPORT`, `TRAIN_STATION`, `BUS_TERMINAL`, `HELIPORT`, `LANDING_ZONE` |
| notification | `NotificationType` | `BOOKING_CONFIRMED`, `TOUR_APPROVAL_REQUIRED`, `TOUR_APPROVED`, `CANCELLATION_ALERT`, `ONE_WEEK_TRAVEL_REMINDER`, `SYSTEM_ALERT`, `REQUEST_CREATED`, `REQUEST_ASSIGNED`, `REQUEST_SOLVED`, `REQUEST_REJECTED`, `TOUR_COMPLETED` |
| notification | `ReferenceType` | `TOUR`, `RESERVATION`, `TICKET`, `USER`, `USER_REQUEST` |
| payment | `AccountStatus` | `ACTIVE`, `FROZEN`, `CLOSED` |
| payment | `AccountType` | `CUSTOMER_WALLET`, `AGENCY_WALLET`, `SYSTEM_WALLET` |
| payment | `PaymentMethod` | `CREDIT_CARD`, `PAYPAL`, `BANK_TRANSFER`, `CASH_AT_OFFICE`, `WALLET` |
| payment | `PaymentStatus` | `PENDING`, `COMPLETED`, `FAILED`, `REFUNDED` |
| payment | `TransactionType` | `PAYMENT`, `REFUND`, `PARTIAL_REFUND`, `CANCELLATION_FEE`, `WALLET_TOP_UP`, `MANUAL_ADJUSTMENT`, `WITHDRAWAL` |
| support | `UserRequestAction` | `ASSIGN`, `SOLVE`, `REJECT` |
| support | `UserRequestStatus` | `PENDING`, `APPROVED`, `REJECTED`, `CONFIRMED`, `CANCELLED`, `COMPLETED`, `ACTIVE`, `INACTIVE`, `SOLVED`, `UNSOLVED` |
| support | `UserRequestType` | `SUPPORT`, `SUGGESTION` |
| tourmanagement | `ChairType` | `STANDARD`, `KIDS_CHAIR`, `WHEELCHAIR_ACCESSIBLE`, `PREMIUM_RECLINER` |
| tourmanagement | `MealDietaryType` | `STANDARD`, `VEGETARIAN`, `VEGAN`, `GLUTEN_FREE` |
| tourmanagement | `SeatStatus` | `AVAILABLE`, `BOOKED`, `RESERVED`, `MAINTENANCE` |
| tourmanagement | `SpiceLevel` | `NONE`, `MILD`, `MEDIUM`, `HOT`, `EXTRA_HOT` |
| tourmanagement | `TicketStatus` | `PENDING`, `CONFIRMED`, `CANCELLED`, `COMPLETED` |
| tourmanagement | `TransportationStatus` | `AVAILABLE`, `PARTIAL`, `FULL`, `MAINTENANCE`, `INACTIVE` |
| tourmanagement | `TransportationType` | `BUS`, `FLIGHT`, `BOAT`, `TRAIN`, `PRIVATE_CAR`, `FERRY` |
| user | `UserTypeEnum` | `ADMIN`, `MANAGER`, `EMPLOYEE`, `OWNER`, `CUSTOMER`, `SUPPORT_AGENT`, `DEVELOPER` |
