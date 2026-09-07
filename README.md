# Fun Travels Tour - Documentation

> Complete technical documentation for the Fun Travels Tour platform.

**Author:** Hussain Al Aradi
[Gmail](mailto:hussainaradi.ha@gmail.com) | [GitHub](https://github.com/HussainALAradi5) | [LinkedIn](https://www.linkedin.com/in/hussainalaradi/)

---

## Project Overview

Fun Travels Tour is a full-stack travel agency management platform supporting multi-agency operations, tour lifecycle management, digital ticketing, wallet-based payments, and real-time notifications.

---

## Repositories

| Repository | Tech Stack | Description |
|------------|------------|-------------|
| [Server](server-side/) | Java 21, Spring Boot 3.4, PostgreSQL | Backend API |
| [Client](client-side/) | React 19, TypeScript, Vite, Chakra UI | Web frontend |
| Mobile | React Native, Expo SDK 54 | Mobile app (docs coming soon) |

---

## Documentation Structure

```
fun-travels-tour-document/
├── README.md                    # This file
├── server-side/                 # Backend documentation
│   ├── README.md               # Server overview
│   ├── user-management/        # Auth, users, accounts
│   │   ├── models/
│   │   ├── services/
│   │   └── endpoints/
│   ├── agency-management/      # Agencies, branches
│   ├── tour-management/        # Tours, tickets, seats, meals, transport
│   ├── payment-management/     # Payments, transactions, wallet
│   ├── geography-management/   # Countries, cities, ports
│   ├── notification-management/# Real-time notifications
│   └── support-management/     # Support requests, comments, audit
│
└── client-side/                # Frontend documentation
    ├── README.md               # Client overview
    ├── user-management/        # Auth, profile, user admin
    │   ├── components/
    │   ├── services/
    │   ├── interfaces/
    │   ├── hooks/
    │   └── pages/
    ├── agency-management/      # Agency UI
    ├── tour-management/        # Tour UI, booking flow
    ├── payment-management/     # Payment UI, wallet
    ├── geography-management/   # Country/city UI
    ├── notification-management/# Notification UI
    ├── support-management/     # Support request UI
    └── ui-components/          # Reusable generic components
```

---

## User Roles

| Role | Description |
|------|-------------|
| `ADMIN` | Full system access |
| `OWNER` | Agency owner |
| `MANAGER` | Branch manager |
| `EMPLOYEE` | Operations staff |
| `CUSTOMER` | End user / traveler |
| `SUPPORT_AGENT` | Support staff |
