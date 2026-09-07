# Agency Management (Client)

## Components
- AgencyDetail, AgencyTable, BranchTab, BranchTable, EmployeeTab
- AddAgencyDialog, AddBranchDialog, AddEmployeesAction

## Services
- agencyService, branchService

## Hooks
- useAgencies

## Routes
| Route | Page | Access |
|-------|------|--------|
| /admin/agencies | AgencyNetworkPage | ADMIN |
| /admin/agencies/:id | AgencyDetail | ADMIN |
