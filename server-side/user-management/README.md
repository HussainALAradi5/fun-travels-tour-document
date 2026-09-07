# User Management

Handles authentication, user accounts, and wallet management.

## Entities
- **User** - System user with roles (ADMIN, MANAGER, EMPLOYEE, OWNER, CUSTOMER, SUPPORT_AGENT)
- **Account** - User wallet for financial operations

## Services
- [AuthService](services/AuthService.md) - Login, registration, password reset
- [UserService](services/UserService.md) - User CRUD, employee management, bulk import
- [AccountService](services/AccountService.md) - Wallet balance, history

## Endpoints
- [AuthController](endpoints/AuthController.md) - `/api/auth`
- [UserController](endpoints/UserController.md) - `/api/users`
- [AccountController](endpoints/AccountController.md) - `/api/accounts`
- [WalletController](endpoints/WalletController.md) - `/api/wallet`

## Business Logic
- Passwords are BCrypt hashed before storage
- JWT tokens are generated on login/register
- Users can be assigned to agencies and branches
- Bulk import supports Excel files (.xlsx)
- Accounts are created automatically on user registration
