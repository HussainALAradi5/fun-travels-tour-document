# Notification Management Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Receive a domain event or user query. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Resolve the recipient and reference metadata. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Build title, message, type, and read state. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Persist or query notification records. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Return notification DTOs/counts. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. Validation occurs before irreversible state changes.
2. Related writes succeed or roll back together.
3. Domain events, notifications, and audit records follow the committed state.
4. Retry behavior must not duplicate charges, inventory, or terminal transitions.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.

