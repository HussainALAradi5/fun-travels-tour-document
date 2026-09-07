# AuthController

**File:** `src/main/java/com/server/server/controllers/AuthController.java`
**Base Path:** `/api/auth`

## Endpoints

### POST /api/auth/register

**Description:** Register a new user account

**Service Method:** `UserService.createUser(User)`

**Request Body:**
```json
{
  "userName": "string (required, unique)",
  "name": "string (required)",
  "email": "string (required, unique)",
  "password": "string (required)",
  "mobileNumber": "string (unique)",
  "age": 0
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "User registered successfully!",
  "data": {
    "id": 1,
    "userName": "...",
    "name": "...",
    "email": "...",
    "userType": "CUSTOMER",
    "active": true
  }
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "message": "Email taken"
}
```

**Exceptions:**
| Status | Condition |
|--------|-----------|
| 400 | Email taken, Username taken, missing required fields |

**Access:** Public

---

### POST /api/auth/login

**Description:** Authenticate user and get JWT token

**Service Method:** `AuthenticationManager.authenticate()` + `JwtService.generateToken()`

**Request Body:**
```json
{
  "identifier": "email_or_username_or_mobile",
  "password": "string"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "userName": "...",
    "email": "...",
    "userType": "CUSTOMER"
  }
}
```

**Response (401 Unauthorized):**
```json
{
  "success": false,
  "message": "Invalid email/username or password"
}
```

**Exceptions:**
| Status | Condition |
|--------|-----------|
| 401 | BadCredentialsException - invalid credentials |
| 400 | User data not found after authentication |

**Access:** Public
