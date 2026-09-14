# JWT Service

**Source:** `src/main/java/com/server/server/services/JwtService.java`

## Function reference

| Function | Signature | Parameters | Function logic | Business logic | Return value | Side effects and exceptions |
|---|---|---|---|---|---|---|
| `extractUsername` | `public String extractUsername(String token)` | Signed JWT | Extracts the subject claim through `extractClaim`. | The email subject identifies the authenticated principal. | Username/email. | Stateless; malformed, expired, or invalid signatures propagate JJWT exceptions. |
| `generateToken` | `public String generateToken(String email)` | Authenticated email | Sets subject, issued time, 24-hour expiry, signs, and compacts. | Authentication sessions expire after one day. | Signed JWT. | Stateless; signing failures propagate. |
| `isTokenValid` | `public boolean isTokenValid(String token, UserDetails userDetails)` | Token and expected principal | Requires matching username and a non-expired token. | Prevents token reuse for a different account. | Validation boolean. | Invalid token parsing may propagate JJWT exceptions. |
| `isTokenExpired` | `private boolean isTokenExpired(String token)` | Token | Reads expiry and compares it with current time. | Enforces session lifetime. | `true` when expired. | No direct exception; parsing failures propagate. |
| `extractClaim` | `public <T> T extractClaim(String token, Function<Claims,T> claimsResolver)` | Token and claim resolver | Verifies signature, parses claims, and applies the resolver. | Centralizes cryptographic verification. | Requested claim. | JJWT verification/parsing exceptions. |
| `getSignInKey` | `private SecretKey getSignInKey()` | None | Base64-decodes the configured secret and creates an HMAC key. | Ensures generation and validation use the same signing key. | `SecretKey`. | Key decoding/strength errors may propagate. |

No function performs database writes. Authentication filters translate token failures into the HTTP security response.
