# Fun Travels Tour - Client Documentation

Web frontend for the Fun Travels Tour travel agency management platform.

**Tech:** React 19 | TypeScript | Vite 7 | Chakra UI v3

## Quick Start

```bash
npm install
npm run dev
```

App starts at `http://localhost:5173`

## Architecture

```
src/
├── Api/              # API service layer (19 files)
├── components/       # UI components (90+ files)
│   ├── ui/Custom/    # Reusable generic components (30+ files)
│   ├── TourManagement/
│   ├── Agency/
│   └── User/
├── config/           # Axios base configuration
├── enums/            # TypeScript enums (17 files)
├── hooks/            # Custom React hooks (11 files)
├── interface/        # TypeScript interfaces (18 files)
├── pages/            # Route pages (26 files)
└── utilities/        # Helpers, contexts, utils
```

## Domain Modules

| Module | Description |
|--------|-------------|
| [User Management](user-management/) | Auth, profile, user admin |
| [Agency Management](agency-management/) | Agencies and branches |
| [Tour Management](tour-management/) | Tours, transport, tickets, seats, meals, booking |
| [Payment Management](payment-management/) | Payments, transactions, wallet |
| [Geography Management](geography-management/) | Countries, cities, ports |
| [Notification Management](notification-management/) | Real-time notifications |
| [Support Management](support-management/) | Support requests |
| [UI Components](ui-components/) | Reusable generic components |

## State Management
- AuthContext - User authentication state
- NotificationContext - WebSocket-based real-time notifications
- Custom Hooks - Domain-specific data fetching
