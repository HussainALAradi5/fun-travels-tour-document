# AuthController

**File:** `src/main/java/com/server/server/controllers/AuthController.java`
**Base Path:** `/api/auth`

## Endpoints

### POST /api/auth/register
Register a new user account.

**Request Body:**
```json
{
  "userName": "string",
  "name": "string",
  "email": "string",
  "password": "string",
  "mobileNumber": "string",
  "age": 0
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Registration successful",
  "data": {
    "token": "jwt_token",
    "user": { }
  }
}
```

### POST /api/auth/login
Authenticate user.

**Request Body:**
```json
{
  "identifier": "email_or_username_or_mobile",
  "password": "string"
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "token": "jwt_token",
    "user": { }
  }
}
```

### POST /api/auth/request-password-reset
Request password reset code.

### POST /api/auth/confirm-password-reset
Confirm reset with code.

## Access
All endpoints are **public** (no authentication required).
