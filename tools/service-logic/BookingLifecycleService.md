## Business logic

Shared by customer cancellation, hold expiry, staff rejection, and agency tour cancellation, so all four end a booking the same way.

- `activeTickets` - tickets that are not CANCELLED.
- `activeTotal` - sum of active ticket prices; reservations created before tickets existed use their stored total.
- `releaseAndCancelTickets` - releases one place per active ticket (or `requestedSlots` for legacy reservations) and marks them cancelled with the given approval status.
- `refundToWallet` - credits the customer's wallet only for positive amounts.

| Case | Result |
| --- | --- |
| One of three tickets cancelled earlier, reservation then cancelled | Only the two active tickets are refunded and released |
| Legacy reservation without tickets | `requestedSlots` places released, stored total refunded |
