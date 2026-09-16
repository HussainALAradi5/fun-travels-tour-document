# User, Authentication, and Account Management Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Validate identity fields and uniqueness. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Encode or verify the password. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Create/update user, role, agency, branch, and account relationships. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Issue JWT or reset communication when applicable. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Return a sanitized user response or clear authentication error. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. Validation occurs before irreversible state changes.
2. Related writes succeed or roll back together.
3. Domain events, notifications, and audit records follow the committed state.
4. Retry behavior must not duplicate charges, inventory, or terminal transitions.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.

