# Services

Every public function in source order: signature, purpose, transaction and role notes, and the cases it rejects with their exception and status (its own throws and those of the private helpers it calls). Services marked *business logic* also carry hand-written rules.

| Domain | Service | Functions | Business logic |
| --- | --- | --- | --- |
| agency | [AgencyBranchService](agency/AgencyBranchService.md) | 5 | yes |
| agency | [AgencyService](agency/AgencyService.md) | 6 | yes |
| auth | [AccessPolicyService](auth/AccessPolicyService.md) | 12 | yes |
| auth | [AuthService](auth/AuthService.md) | 4 | yes |
| auth | [JwtService](auth/JwtService.md) | 3 | - |
| common | [CodeGenerationService](common/CodeGenerationService.md) | 2 | - |
| common | [ExcelImportService](common/ExcelImportService.md) | 2 | - |
| common | [FileStorageService](common/FileStorageService.md) | 5 | - |
| common | [GenericFilterService](common/GenericFilterService.md) | 3 | - |
| common | [SystemSchedulingService](common/SystemSchedulingService.md) | 2 | - |
| geography | [CityService](geography/CityService.md) | 4 | - |
| geography | [CountryService](geography/CountryService.md) | 6 | - |
| geography | [PortService](geography/PortService.md) | 4 | - |
| media | [MediaService](media/MediaService.md) | 5 | yes |
| notification | [NotificationService](notification/NotificationService.md) | 8 | - |
| payment | [AccountService](payment/AccountService.md) | 4 | - |
| payment | [PaymentService](payment/PaymentService.md) | 3 | yes |
| payment | [TransactionService](payment/TransactionService.md) | 4 | yes |
| payment | [WalletTopUpService](payment/WalletTopUpService.md) | 1 | yes |
| report | [ReportDataService](report/ReportDataService.md) | 1 | yes |
| report | [ReportService](report/ReportService.md) | 1 | yes |
| support | [GenericTrackingService](support/GenericTrackingService.md) | 4 | yes |
| support | [UserRequestService](support/UserRequestService.md) | 7 | - |
| tourmanagement | [BookingLifecycleService](tourmanagement/BookingLifecycleService.md) | 4 | yes |
| tourmanagement | [InventoryService](tourmanagement/InventoryService.md) | 5 | yes |
| tourmanagement | [MealPlanService](tourmanagement/MealPlanService.md) | 6 | yes |
| tourmanagement | [SeatService](tourmanagement/SeatService.md) | 5 | yes |
| tourmanagement | [TicketIssuingService](tourmanagement/TicketIssuingService.md) | 3 | yes |
| tourmanagement | [TicketService](tourmanagement/TicketService.md) | 8 | yes |
| tourmanagement | [TourCatalogService](tourmanagement/TourCatalogService.md) | 4 | yes |
| tourmanagement | [TourReservationService](tourmanagement/TourReservationService.md) | 9 | yes |
| tourmanagement | [TourSchedulerService](tourmanagement/TourSchedulerService.md) | 2 | yes |
| tourmanagement | [TourService](tourmanagement/TourService.md) | 3 | yes |
| tourmanagement | [TourStatusService](tourmanagement/TourStatusService.md) | 1 | yes |
| tourmanagement | [TransportationImportService](tourmanagement/TransportationImportService.md) | 1 | yes |
| tourmanagement | [TransportationService](tourmanagement/TransportationService.md) | 7 | yes |
| user | [ProfileService](user/ProfileService.md) | 2 | yes |
| user | [UserService](user/UserService.md) | 11 | yes |
