# Client Documentation

The web client is a server-rendered Next.js application for customer booking and internal travel operations.

**Stack:** Next.js 16.3 · React 19.2 · TypeScript 5.9 · Chakra UI 3.37 · Axios · STOMP · Stripe

## Commands

```bash
npm install
npm run dev
npm run build
npm run lint
```

The development client starts at `http://localhost:3000` unless configured otherwise.

## Design principles

- Domain interfaces are used for relations (`Partial<Agency>`, `Partial<AgencyBranch>`, and similar) instead of ambiguous generic summaries.
- No `any` types are introduced in API or component contracts.
- API access is isolated under `src/Api` and uses a shared response/error convention.
- Reusable Chakra UI components support responsive light and dark themes.
- Expensive form controls are memoized so unrelated fields do not rerender on each keystroke.
- Server-rendered markup remains deterministic to prevent hydration mismatches.

## Main routes

| Route | Purpose |
|---|---|
| `/tours` | Customer tour catalog and booking guide |
| `/reserve/[tourId]` | Reservation workflow |
| `/my-bookings` | Customer tickets and usage guide |
| `/admin/tours` | Tour operations |
| `/admin/transports` | Fleet, Excel import, and seat management |
| `/components` | Reusable component showcase |
