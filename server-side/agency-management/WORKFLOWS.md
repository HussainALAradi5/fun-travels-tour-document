# Agency Management Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Validate authenticated role and request input. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Resolve agency, geography, owner, branch, or manager references. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Apply uniqueness and ownership rules. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Persist inside a transaction. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Map the entity to an API response or a stable error. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. Validation occurs before irreversible state changes.
2. Related writes succeed or roll back together.
3. Domain events, notifications, and audit records follow the committed state.
4. Retry behavior must not duplicate charges, inventory, or terminal transitions.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.

