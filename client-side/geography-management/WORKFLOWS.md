# Geography UI Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Load countries or active ports. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Store the selected parent. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Clear stale dependent selections. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Request cities for the country. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Submit normalized IDs. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. The server response is authoritative after mutations.
2. Dependent selections clear when their parent changes.
3. Submissions are disabled while pending.
4. Only affected query caches are invalidated.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.

