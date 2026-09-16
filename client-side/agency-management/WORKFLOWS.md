# Agency Management UI Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Render the authorized screen or selector. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Load the first server page with an empty query. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Debounce search and request page zero. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Load additional pages without duplicates. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Submit IDs while retaining typed objects. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. The server response is authoritative after mutations.
2. Dependent selections clear when their parent changes.
3. Submissions are disabled while pending.
4. Only affected query caches are invalidated.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.

