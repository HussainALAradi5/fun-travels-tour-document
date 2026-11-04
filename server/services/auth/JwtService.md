# JwtService

Source: `services/auth/JwtService.java`.

Issues and verifies HS256 tokens signed with the configured `jwt.secret`.

## Functions

### `String extractUsername(String token)`

### `String generateToken(String email)`

### `boolean isTokenValid(String token, UserDetails userDetails)`
