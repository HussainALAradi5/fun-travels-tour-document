# Tour, Booking, Ticket, and Inventory UI Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Render hydration-safe forms and load options. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Keep local inputs responsive. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Submit through typed services. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Show hold, payment, or operational result. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Invalidate affected queries. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. The server response is authoritative after mutations.
2. Dependent selections clear when their parent changes.
3. Submissions are disabled while pending.
4. Only affected query caches are invalidated.

## Booking and payment behavior

1. The client submits the selected travelers, meals, and seats to create a 15-minute pending reservation hold.
2. The checkout then requests wallet payment using the returned reservation ID.
3. Only a server response with a confirmed reservation is presented as a successful booking.
4. If payment fails, the page keeps the pending reservation ID and presents `Retry Wallet Payment` while explaining the remaining hold.
5. Customer ticket lifecycle controls are read-only; cancellation is the only customer mutation and displays the full/partial/no-refund windows.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.
