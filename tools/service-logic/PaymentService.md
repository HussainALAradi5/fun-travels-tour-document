## Business logic

- `executeTransaction` reuses an existing COMPLETED payment for the reservation (idempotent retry); otherwise creates one. Wallet payments debit the wallet and complete immediately; card/PayPal/bank/cash stay PENDING.
- `getById` and `filter` are scoped: customers see payments of their reservations, agency staff those of their agency's tours, wallet top-up payments only admins.
