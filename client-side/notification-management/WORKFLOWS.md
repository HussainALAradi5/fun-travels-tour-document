# Notification UI Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Load counts and notifications. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Render type, message, time, and read state. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Mark the selected item read. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Update counts and navigate if requested. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Show retry feedback on failure. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. The server response is authoritative after mutations.
2. Dependent selections clear when their parent changes.
3. Submissions are disabled while pending.
4. Only affected query caches are invalidated.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.

