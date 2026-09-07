# User Management (Client)

Authentication, user profile, and admin user management.

## Components
- [LoginForm](components/LoginForm.md) - Login form
- [RegisterForm](components/RegisterForm.md) - Registration form
- [ProfileView](components/ProfileView.md) - Profile display
- [EditProfile](components/EditProfile.md) - Profile editing
- [UserManagement](components/UserManagement.md) - Admin user list

## Services
- [userService](services/userService.md) - All user/auth API calls

## Interfaces
- [UserInterface](interfaces/UserInterface.md) - User type definitions

## Hooks
- [useUser](hooks/useUser.md) - User state hook

## Routes
| Route | Page | Access |
|-------|------|--------|
| /login | LoginPage | Public |
| /register | RegisterPage | Public |
| /profile | ProfilePage | Private |
| /admin/users | UsersPage | ADMIN |
