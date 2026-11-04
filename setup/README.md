# Setup

## Server

Requirements: Java 21+ (built and tested with JDK 25), PostgreSQL 15+.

```bash
createdb fun_travels_tour
cp src/main/resources/application.properties.example src/main/resources/application.properties
# set DB_*, JWT_SECRET (32+ chars), and optionally SEED_PASSWORD
./mvnw test
./mvnw spring-boot:run
```

The API listens on `http://localhost:8080` (`SERVER_PORT`).

## Web client

```bash
cp .env.example .env.local      # NEXT_PUBLIC_API_BASE_URL=http://localhost:8080/api
npm ci
npm run dev                     # http://localhost:3000
npm run build && npm run lint
```

## Mobile app

```bash
cp .env.example .env            # EXPO_PUBLIC_API_URL=http://10.0.2.2:8080 (Android emulator)
npm install                     # .npmrc enables legacy peer resolution for Expo SDK 58
npx expo start                  # press a for Android, i for iOS, or scan with Expo Go
npx tsc --noEmit && npx expo lint
```

Use `http://localhost:8080` for the iOS simulator and your computer's LAN IP for a physical device; add that origin to `CORS_ALLOWED_ORIGINS` only if you also use the web build.

## Seeded accounts

With `app.seed.enabled=true` on an empty database: `admin`, `owner`, `manager`, `employee`, `customer`, `support`, `developer` (emails `<name>@funtravel.com`), all with the `SEED_PASSWORD` value or the generated password in `seed-credentials.local.txt`. Owner, manager, and employee belong to the seeded agency "Al Aradi Travel".
