# Tour, Booking, Ticket, and Inventory Management Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Validate role, tour state, dates, capacity, and request relationships. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Lock tour and selected seats before changing inventory. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Create a pending reservation, tickets, prices, codes, and hold expiry. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Execute payment and transition all related records on success. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | On cancellation/expiry, refund when eligible and release all inventory. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. Validation occurs before irreversible state changes.
2. Related writes succeed or roll back together.
3. Domain events, notifications, and audit records follow the committed state.
4. Retry behavior must not duplicate charges, inventory, or terminal transitions.

## Authoritative lifecycle rules

- A reservation is confirmed only by successful payment; the administrative status command cannot approve or confirm it.
- Rejecting a pending reservation cancels its tickets, clears its hold, and releases held capacity and seats.
- Completing a confirmed reservation completes every non-cancelled ticket.
- Cancelling a tour cancels affected reservations and tickets, releases seats, refunds confirmed bookings to customer wallets, and notifies customers atomically.
- Ticket seat changes lock and validate the replacement seat before releasing the current seat.
- Customer ticket workflow indicators are read-only; customers may cancel their own ticket but cannot approve, confirm, or complete it.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.
