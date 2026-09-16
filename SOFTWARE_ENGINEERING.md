# Software Engineering Documentation

This index connects the requirements, use cases, workflow specifications, and maintainable Mermaid flowcharts for every feature boundary.

See [System Personas](PERSONAS.md) for the named actors used consistently throughout the use cases.

## Document purpose

| Artifact | Purpose |
|---|---|
| Requirements | Defines functional, business, quality, security, and usability expectations. |
| Use cases | Connects actors and preconditions to success and alternate outcomes. |
| Workflows | Describes ordered processing, state rules, transactions, and failure behavior. |
| Flowcharts | Visualizes primary paths, decisions, rollback, and API/UI state changes. |

## Server modules

| Module | Requirements | Use cases | Workflows | Flowcharts |
|---|---|---|---|---|
| Agency Management | [Requirements](server-side/agency-management/REQUIREMENTS.md) | [Use cases](server-side/agency-management/USE_CASES.md) | [Workflows](server-side/agency-management/WORKFLOWS.md) | [Flowcharts](server-side/agency-management/FLOWCHARTS.md) |
| Geography Management | [Requirements](server-side/geography-management/REQUIREMENTS.md) | [Use cases](server-side/geography-management/USE_CASES.md) | [Workflows](server-side/geography-management/WORKFLOWS.md) | [Flowcharts](server-side/geography-management/FLOWCHARTS.md) |
| Notification Management | [Requirements](server-side/notification-management/REQUIREMENTS.md) | [Use cases](server-side/notification-management/USE_CASES.md) | [Workflows](server-side/notification-management/WORKFLOWS.md) | [Flowcharts](server-side/notification-management/FLOWCHARTS.md) |
| Payment Management | [Requirements](server-side/payment-management/REQUIREMENTS.md) | [Use cases](server-side/payment-management/USE_CASES.md) | [Workflows](server-side/payment-management/WORKFLOWS.md) | [Flowcharts](server-side/payment-management/FLOWCHARTS.md) |
| Platform Services | [Requirements](server-side/platform-services/REQUIREMENTS.md) | [Use cases](server-side/platform-services/USE_CASES.md) | [Workflows](server-side/platform-services/WORKFLOWS.md) | [Flowcharts](server-side/platform-services/FLOWCHARTS.md) |
| Support Management | [Requirements](server-side/support-management/REQUIREMENTS.md) | [Use cases](server-side/support-management/USE_CASES.md) | [Workflows](server-side/support-management/WORKFLOWS.md) | [Flowcharts](server-side/support-management/FLOWCHARTS.md) |
| Tour Management | [Requirements](server-side/tour-management/REQUIREMENTS.md) | [Use cases](server-side/tour-management/USE_CASES.md) | [Workflows](server-side/tour-management/WORKFLOWS.md) | [Flowcharts](server-side/tour-management/FLOWCHARTS.md) |
| User Management | [Requirements](server-side/user-management/REQUIREMENTS.md) | [Use cases](server-side/user-management/USE_CASES.md) | [Workflows](server-side/user-management/WORKFLOWS.md) | [Flowcharts](server-side/user-management/FLOWCHARTS.md) |

## Client modules

| Module | Requirements | Use cases | Workflows | Flowcharts |
|---|---|---|---|---|
| Agency UI | [Requirements](client-side/agency-management/REQUIREMENTS.md) | [Use cases](client-side/agency-management/USE_CASES.md) | [Workflows](client-side/agency-management/WORKFLOWS.md) | [Flowcharts](client-side/agency-management/FLOWCHARTS.md) |
| Geography UI | [Requirements](client-side/geography-management/REQUIREMENTS.md) | [Use cases](client-side/geography-management/USE_CASES.md) | [Workflows](client-side/geography-management/WORKFLOWS.md) | [Flowcharts](client-side/geography-management/FLOWCHARTS.md) |
| Notification UI | [Requirements](client-side/notification-management/REQUIREMENTS.md) | [Use cases](client-side/notification-management/USE_CASES.md) | [Workflows](client-side/notification-management/WORKFLOWS.md) | [Flowcharts](client-side/notification-management/FLOWCHARTS.md) |
| Payment UI | [Requirements](client-side/payment-management/REQUIREMENTS.md) | [Use cases](client-side/payment-management/USE_CASES.md) | [Workflows](client-side/payment-management/WORKFLOWS.md) | [Flowcharts](client-side/payment-management/FLOWCHARTS.md) |
| Support UI | [Requirements](client-side/support-management/REQUIREMENTS.md) | [Use cases](client-side/support-management/USE_CASES.md) | [Workflows](client-side/support-management/WORKFLOWS.md) | [Flowcharts](client-side/support-management/FLOWCHARTS.md) |
| Tour UI | [Requirements](client-side/tour-management/REQUIREMENTS.md) | [Use cases](client-side/tour-management/USE_CASES.md) | [Workflows](client-side/tour-management/WORKFLOWS.md) | [Flowcharts](client-side/tour-management/FLOWCHARTS.md) |
| UI Components | [Requirements](client-side/ui-components/REQUIREMENTS.md) | [Use cases](client-side/ui-components/USE_CASES.md) | [Workflows](client-side/ui-components/WORKFLOWS.md) | [Flowcharts](client-side/ui-components/FLOWCHARTS.md) |
| User UI | [Requirements](client-side/user-management/REQUIREMENTS.md) | [Use cases](client-side/user-management/USE_CASES.md) | [Workflows](client-side/user-management/WORKFLOWS.md) | [Flowcharts](client-side/user-management/FLOWCHARTS.md) |

## Traceability

Business behavior is authoritative in server requirements and service documentation. Client requirements describe presentation and interaction obligations. Endpoint mappings connect client use cases to server functions, while workflow and flowchart documents show state transitions and failure paths.
