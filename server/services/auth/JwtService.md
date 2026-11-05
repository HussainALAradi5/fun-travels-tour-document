# JwtService

Source: `services/auth/JwtService.java`.

Issues and verifies HS256 tokens signed with the configured `jwt.secret`.

## Functions

### `String extractUsername(String token)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `String generateToken(String email)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `boolean isTokenValid(String token, UserDetails userDetails)`

**Exceptions:** none of its own; failures come from the functions it calls.
