# Reusable UI Components Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Receive typed props and stable state. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Render semantic SSR-safe HTML. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Handle interaction states. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Emit typed events. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Clean up listeners and dialogs. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. The server response is authoritative after mutations.
2. Dependent selections clear when their parent changes.
3. Submissions are disabled while pending.
4. Only affected query caches are invalidated.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.

