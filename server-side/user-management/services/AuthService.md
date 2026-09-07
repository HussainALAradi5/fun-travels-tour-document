# AuthService

**File:** `src/main/java/com/server/server/services/AuthService.java`

## Code

```java
@Service
@RequiredArgsConstructor
public class AuthService {
    private final UserRepository repository;
    private final JwtService jwtService;
    private final AuthenticationManager authenticationManager;

    public String authenticate(String email, String password) {
        authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(email, password));
        return jwtService.generateToken(email);
    }
}
```

## Methods

### authenticate(email, password) -> String

**Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| email | String | User email, username, or mobile number |
| password | String | Plain text password |

**Returns:** JWT token string

**Business Logic:**
1. Spring Security's AuthenticationManager validates credentials
2. BCrypt password hash is compared automatically
3. If valid, generates JWT token via JwtService

**Exceptions:**
| Exception | Condition |
|-----------|-----------|
| BadCredentialsException | Invalid email/username or password |
| UsernameNotFoundException | User not found in database |

**Dependencies:**
- UserRepository
- JwtService
- AuthenticationManager (Spring Security)
