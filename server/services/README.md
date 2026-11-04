# Services

Every public function with its signature, generated from the source. Services marked *business logic* also carry hand-written rules, cases, and exceptions.

| Domain | Service | Functions | Business logic |
| --- | --- | --- | --- |
| agency | [AgencyBranchService](agency/AgencyBranchService.md) | 5 | - |
| agency | [AgencyService](agency/AgencyService.md) | 5 | - |
| auth | [AccessPolicyService](auth/AccessPolicyService.md) | 10 | yes |
| auth | [AuthService](auth/AuthService.md) | 4 | yes |
| auth | [JwtService](auth/JwtService.md) | 3 | - |
| common | [CodeGenerationService](common/CodeGenerationService.md) | 2 | - |
| common | [ExcelImportService](common/ExcelImportService.md) | 2 | - |
| common | [FileStorageService](common/FileStorageService.md) | 2 | - |
| common | [GenericFilterService](common/GenericFilterService.md) | 3 | - |
| common | [SystemSchedulingService](common/SystemSchedulingService.md) | 2 | - |
| geography | [CityService](geography/CityService.md) | 4 | - |
| geography | [CountryService](geography/CountryService.md) | 6 | - |
| geography | [PortService](geography/PortService.md) | 4 | - |
| notification | [NotificationService](notification/NotificationService.md) | 8 | - |
| payment | [AccountService](payment/AccountService.md) | 4 | - |
| payment | [PaymentService](payment/PaymentService.md) | 3 | yes |
| payment | [TransactionService](payment/TransactionService.md) | 4 | yes |
| payment | [WalletTopUpService](payment/WalletTopUpService.md) | 1 | yes |
| support | [GenericTrackingService](support/GenericTrackingService.md) | 4 | yes |
| support | [UserRequestService](support/UserRequestService.md) | 7 | - |
| tourmanagement | [BookingLifecycleService](tourmanagement/BookingLifecycleService.md) | 4 | yes |
| tourmanagement | [InventoryService](tourmanagement/InventoryService.md) | 4 | yes |
| tourmanagement | [MealPlanService](tourmanagement/MealPlanService.md) | 7 | yes |
| tourmanagement | [SeatService](tourmanagement/SeatService.md) | 5 | yes |
| tourmanagement | [TicketIssuingService](tourmanagement/TicketIssuingService.md) | 3 | yes |
| tourmanagement | [TicketService](tourmanagement/TicketService.md) | 8 | yes |
| tourmanagement | [TourReservationService](tourmanagement/TourReservationService.md) | 9 | yes |
| tourmanagement | [TourService](tourmanagement/TourService.md) | 9 | yes |
| tourmanagement | [TransportationService](tourmanagement/TransportationService.md) | 8 | yes |
| user | [ProfileService](user/ProfileService.md) | 2 | yes |
| user | [UserService](user/UserService.md) | 11 | yes |
