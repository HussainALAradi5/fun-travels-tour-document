# Fun Travels Tour - Server Documentation

Backend API for the Fun Travels Tour travel agency management platform.

**Tech:** Java 21 | Spring Boot 3.4.13 | PostgreSQL | JWT | Stripe

## Quick Start

```bash
# Prerequisites: Java 21+, PostgreSQL 15+

# 1. Create database
createdb fun_travels_tour

# 2. Configure src/main/resources/application.properties
spring.datasource.url=jdbc:postgresql://localhost:5432/fun_travels_tour
spring.datasource.username=your_user
spring.datasource.password=your_pass
spring.jpa.hibernate.ddl-auto=update
jwt.secret=your_secret_key
stripe.api.secret-key=sk_test_xxx
stripe.api.publishable-key=pk_test_xxx

# 3. Run
./mvnw spring-boot:run
```

Server starts at `http://localhost:8080`

## Architecture

```
com.server.server/
├── Config/           # Security, JWT, CORS, Stripe, WebSocket, Audit
├── controllers/      # REST API endpoints (20 controllers)
├── Models/           # JPA entities (19 entities)
├── repositories/     # Spring Data JPA repositories (19 repos)
├── services/         # Business logic (27 services)
├── enums/            # Type enumerations (17 enums)
├── exceptions/       # Global error handling
└── utilities/        # ApiResponse wrapper
```

## Domain Modules

| Module | Entities | Services | Endpoints |
|--------|----------|----------|-----------|
| [User Management](user-management/) | User, Account | AuthService, UserService, AccountService | Auth, User, Account, Wallet |
| [Agency Management](agency-management/) | Agency, AgencyBranch | AgencyService, AgencyBranchService | Agency, AgencyBranch |
| [Tour Management](tour-management/) | Tour, Transportation, Seat, MealPlan, TourReservation, Ticket | TourService, TransportationService, SeatService, MealPlanService, TourReservationService, TicketService | Tour, Transportation, Seat, MealPlan, TourReservation, Ticket |
| [Payment Management](payment-management/) | Payment, Transaction | PaymentService, TransactionService, PaymentProcessingService, WalletTopUpService | Payment, Transaction, Wallet |
| [Geography Management](geography-management/) | Country, City, Port | CountryService, CityService, PortService | Country, City, Port |
| [Notification Management](notification-management/) | Notification | NotificationService | Notification |
| [Support Management](support-management/) | UserRequest, GenericComment, GenericEventLog | UserRequestService, GenericTrackingService | UserRequest, GenericTracking |

## User Roles

| Role | Access Level |
|------|-------------|
| ADMIN | Full system access |
| OWNER | Agency owner - manages branches, employees, tours |
| MANAGER | Branch manager - manages tours and reservations |
| EMPLOYEE | Day-to-day operations |
| CUSTOMER | Books tours, views tickets, makes payments |
| SUPPORT_AGENT | Handles support requests |

## Security

- JWT token-based authentication (stateless)
- BCrypt password hashing
- CORS: localhost, Android emulator (10.0.2.2)
- WebSocket: STOMP at /ws-notifications

## External Integrations

| Service | Purpose |
|---------|---------|
| Stripe | Payment processing |
| Twilio | SMS/WhatsApp messaging |
| RestCountries API | Country data sync |
| ZXing | QR code / barcode generation |
