# AuthService

**File:** `src/main/java/com/server/server/services/AuthService.java`

Handles user authentication and registration.

## Methods

### register(RegisterRequest) -> AuthResponse
Creates a new user account.
- Validates unique username and email
- Hashes password with BCrypt
- Creates associated Account (wallet)
- Generates JWT token
- Returns token + user data

### login(LoginRequest) -> AuthResponse
Authenticates user by email, username, or mobile number.
- Looks up user by identifier (case-insensitive)
- Validates password against BCrypt hash
- Generates JWT token
- Returns token + user data

### requestPasswordReset(email) -> void
Initiates password reset flow.
- Generates 6-digit reset code
- Sends code via email
- Code expires after 15 minutes

### confirmPasswordReset(email, code, newPassword) -> void
Completes password reset.
- Validates reset code
- Updates password (BCrypt hashed)
- Invalidates reset code

## Dependencies
- UserRepository
- AccountRepository
- JwtService
- PasswordEncoder (BCrypt)
