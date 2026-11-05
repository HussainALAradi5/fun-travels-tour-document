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

The API listens on `http://localhost:8080/api/v1` (`SERVER_PORT`, `API_PREFIX`). On start-up Flyway applies the scripts in `db/migration`; a database created before migrations is baselined at version 1 and receives the later scripts (see [schema and seeds](../server/globals/schema-and-seeds.md)). Profile pictures are stored under `FILE_UPLOAD_DIR` (public), generated reports under `MEDIA_DIR` (private, default `./media`) and deleted after `REPORT_RETENTION_DAYS` (default 30). Sign-in attempts are limited by `AUTH_RATE_LIMIT` per minute and address. The full settings table is in the server README.

## Web client

```bash
cp .env.example .env.local      # NEXT_PUBLIC_API_BASE_URL=http://localhost:8080/api/v1
npm ci
npm run dev                     # http://localhost:3000
npm run typecheck && npm run lint && npm run build
```

## Mobile app

```bash
cp .env.example .env            # EXPO_PUBLIC_API_URL=http://10.0.2.2:8080 (Android emulator)
npm install                     # .npmrc enables legacy peer resolution for Expo SDK 58
npx expo start                  # press a for Android, i for iOS, or scan with Expo Go
npm run typecheck && npm run lint
```

Use `http://localhost:8080` for the iOS simulator and your computer's LAN IP for a physical device; add that origin to `CORS_ALLOWED_ORIGINS` only if you also use the web build.

## Seeded accounts

With `app.seed.enabled=true` on an empty database: `admin`, `owner`, `manager`, `employee`, `customer`, `support`, `developer` (emails `<name>@funtravel.com`), all with the `SEED_PASSWORD` value or the generated password in `seed-credentials.local.txt`. Owner, manager, and employee belong to the seeded agency "Al Aradi Travel".
