# Agency Management

Manages travel agencies and their branch offices.

## Entities
- **Agency** - Travel agency with owner, location, and contact info
- **AgencyBranch** - Branch office belonging to an agency

## Services
- [AgencyService](services/AgencyService.md) - Agency CRUD, staff management
- [AgencyBranchService](services/AgencyBranchService.md) - Branch CRUD, employee assignment

## Endpoints
- [AgencyController](endpoints/AgencyController.md) - `/api/agencies`
- [AgencyBranchController](endpoints/AgencyBranchController.md) - `/api/branches`

## Business Logic
- Each agency has one owner (User with OWNER role)
- Agencies can have multiple branches
- Employees are assigned to specific branches
- Branch managers can be assigned per branch
- Agencies are linked to a country and city
