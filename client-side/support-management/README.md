# Support Management (Client)

## Components
- UserRequestManagement, UserRequestList, UserRequestDetails, UserRequestCreateDialog

## Services
- userRequestService

## Routes
| Route | Page | Access |
|-------|------|--------|
| /my-requests | UserRequestsPage | Private |
| /my-requests/:id | UserRequestDetailsPage | Private |
| /admin/requests | UserRequestsPage | ADMIN |
