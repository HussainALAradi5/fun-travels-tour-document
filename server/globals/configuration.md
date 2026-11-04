# Configuration

All values come from environment variables through `application.properties` (copy `application.properties.example`). Typed, validated records fail startup on bad values.

| Property | Env variable | Default | Notes |
| --- | --- | --- | --- |
| `spring.datasource.url` | `DB_URL` | `jdbc:postgresql://localhost:5432/fun_travels_tour` | |
| `spring.datasource.username` / `password` | `DB_USERNAME` / `DB_PASSWORD` | - | |
| `jwt.secret` | `JWT_SECRET` | development placeholder | **Required, at least 32 characters** (`JwtProperties`). Change for any shared environment |
| `jwt.expiration` | `JWT_EXPIRATION` | `86400000` (24 h) | milliseconds |
| `app.client-url` | `CLIENT_URL` | `http://localhost:3000` | Used in password-reset links |
| `app.cors-allowed-origins` | `CORS_ALLOWED_ORIGINS` | localhost, 127.0.0.1, 10.0.2.2 (any port) | Also applied to the WebSocket endpoint |
| `app.upload-dir` | `FILE_UPLOAD_DIR` | `./uploads` | Served read-only at `/uploads/**` |
| `app.max-image-bytes` | `MAX_IMAGE_BYTES` | `2097152` | Profile photos: JPEG/PNG only |
| `app.seed.enabled` / `app.seed.password` | `SEED_ENABLED` / `SEED_PASSWORD` | `true` in the example, `false` in code | See [seeds](schema-and-seeds.md) |
| `booking.hold-cleanup-ms` | `BOOKING_HOLD_CLEANUP_MS` | `60000` | Expired-hold sweep interval |
| `stripe.api.secret-key` / `publishable-key` | `STRIPE_SECRET_KEY` / `STRIPE_PUBLISHABLE_KEY` | test placeholders | Wallet top-up by card |
| `api.restcountries.api-key` | `REST_COUNTRIES_API_KEY` | empty | Country sync |
| `spring.mail.*` | `MAIL_*` | Gmail SMTP | Password-reset email |
