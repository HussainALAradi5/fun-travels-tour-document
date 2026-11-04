## Business logic

- Bookings are paid from the wallet only. `executeTransaction` reuses an existing COMPLETED payment for the reservation (idempotent retry); otherwise it debits the wallet and completes at once.
- Any other method fails with 409 `PAYMENT_METHOD_UNSUPPORTED` ("top up your wallet by card, then pay"). There is no provider webhook to complete an external booking payment, so accepting one would leave it pending forever.
- `getById` and `filter` are scoped: customers see payments of their reservations, agency staff those of their agency's tours, wallet top-up payments only admins.
