# Payment and Wallet Management Workflows

## Workflow process catalog

| ID | Process step | Owner | Input | Expected outcome |
|---|---|---|---|---|
| WF-1 | Validate actor, amount, reservation state, and payment method. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-2 | Reuse an existing completed payment when present. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-3 | Execute wallet or provider-specific processing. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-4 | Persist payment and immutable ledger transaction atomically. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |
| WF-5 | Confirm booking or return a safe payment failure. | Application service or current actor | Valid prior-step state | Step completes or returns a traceable error. |

## Process controls

1. Validation occurs before irreversible state changes.
2. Related writes succeed or roll back together.
3. Domain events, notifications, and audit records follow the committed state.
4. Retry behavior must not duplicate charges, inventory, or terminal transitions.

## Traceability

Each WF identifier maps to related RQ and UC identifiers in this module. Workflow changes require corresponding flowchart updates.

