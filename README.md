# Fun Travels Tour Documentation

> Technical and business documentation for a full-stack, multi-agency travel operations platform.

**Author:** Hussain Al Aradi

[Email](mailto:hussainaradi.ha@gmail.com) · [GitHub](https://github.com/HussainALAradi5) · [LinkedIn](https://www.linkedin.com/in/hussainalaradi/)

## Platform overview

Fun Travels Tour manages the operational lifecycle of tours: agency ownership, branches, transportation inventory, generated seats, reservations, passenger tickets, payments, notifications, and customer support. The implementation emphasizes explicit workflow validation, typed API contracts, paginated queries, secure role-based access, and reusable client components.

## Technology

| Application | Stack | Purpose |
|---|---|---|
| [Server](server-side/) | Java 21, Spring Boot 3.5.16, Spring Data JPA, PostgreSQL | REST API and business workflows |
| [Client](client-side/) | Next.js 16.3, React 19, TypeScript 5.9, Chakra UI 3 | Responsive customer and administration portal |
| Mobile | React Native, Expo | Planned mobile client |

## Core capabilities

- Multi-agency and branch-aware operations
- Tour lifecycle and conflict validation
- Transportation inventory with agency/branch ownership
- Bulk Excel transportation import with row-level results
- Automatic and bulk seat-layout generation
- Reservation holds, capacity protection, and ticket issuance
- Payment, transaction, wallet, notification, and support workflows
- Consistent pagination, sorting, date filters, DTO mapping, and API errors
- Accessible, reusable light/dark UI components

## Documentation map

- [Server documentation](server-side/)
- [Complete endpoint reference](server-side/ENDPOINT_REFERENCE.md)
- [Shared platform services](server-side/platform-services/)
- [Client documentation](client-side/)
- [Implementation updates](IMPLEMENTATION_UPDATES.md)
- [Documentation standard](DOCUMENTATION_STANDARD.md)
- [Agency management](server-side/agency-management/)
- [Tour and transportation management](server-side/tour-management/)
- [Payment management](server-side/payment-management/)
- [Reusable UI components](client-side/ui-components/)

## Roles

| Role | Responsibility |
|---|---|
| `ADMIN` | Platform-wide administration |
| `OWNER` | Agency, branch, staff, and inventory ownership |
| `MANAGER` | Branch operations and workflow supervision |
| `EMPLOYEE` | Day-to-day operational work |
| `CUSTOMER` | Tour discovery, booking, payment, and tickets |
| `SUPPORT_AGENT` | Customer-request handling and audit communication |
