# Pricing, discounts, and refunds

All prices and refunds are calculated on the server (`utilities/pricing/PricingCalculator`) from stored records; clients only show an estimate that follows the same rules.

## Ticket price

```text
fare        = tour base price - tour sale discount (discountPrice, never above the base price)
kids chair  = fare x agency kids discount %   (taken off only when the seat is a KIDS_CHAIR)
ticket      = fare - kids chair discount + seat upgrade (seatPriceModifier) + selected meals
reservation = sum of its tickets
```

The kids discount follows the **seat type**, not the traveler's age: bookings carry no traveler ages. The booking screens put children on kids chairs ("Seat my group together"), and travelers without a chosen seat get **standard** seats only, so nobody gets the kids discount, a premium surcharge, or an accessible seat by accident. When no standard seat is left, the booking asks for a seat choice (`SEAT_CHOICE_REQUIRED`).

## Agency policy

Each agency has its own rules (`models/agency/AgencyPolicy`, columns on `agencies`, migration V4). New agencies start with the defaults.

| Setting | Default | Meaning |
| --- | --- | --- |
| `kidsDiscountPercent` | 50 | Taken off the fare on a kids chair (0-100) |
| `fullRefundDays` | 14 | Cancelling more than this many days before the tour refunds everything |
| `partialRefundDays` | 7 | From this many days before the tour, `partialRefundPercent` is refunded |
| `partialRefundPercent` | 50 | Share refunded in the partial window; 0 means no partial refund |

`GET /api/v1/agencies/{id}/policy` is public; tour responses include it as `policy` with a one-line `summary`. Only the agency's owner or an administrator can change it (`PUT /api/v1/agencies/{id}/policy`); the partial window must start no later than the full one. Already paid tickets keep the price they were charged.

## Refunds

| When the customer cancels | Refund |
| --- | --- |
| More than `fullRefundDays` before the tour | 100% |
| From `partialRefundDays` to `fullRefundDays` days before | `partialRefundPercent` |
| Closer than `partialRefundDays` | Nothing |
| The agency cancels the tour | 100%, always |

Only **active** tickets are refunded, so cancelling one ticket and then the reservation never refunds a ticket twice. Before confirming, the apps show `GET /api/v1/reservations/{id}/refund-quote` or `GET /api/v1/tickets/{id}/refund-quote`: what was paid, what would come back, the percentage, the days left, and the rule. The quote uses the same calculation as the cancellation.

## Agency cancellation of a tour

Allowed only 14 or more days before the start and while at most a third of the places are booked (`BookingRules.TOUR_CANCELLATION_MIN_DAYS`, `TOUR_CANCELLATION_MAX_BOOKED_RATIO`); every paid ticket is refunded in full.

## Verified

`business_check` (53 live checks) and `rules_check` (36) cover these rules against a running server: mixed bookings (adult, kids chair, premium seat with a meal), automatic seats, duplicate and taken seats, capacity, holds and their expiry, overlapping dates, refunds at 30, 20, 10 and 3 days under default and custom policies, refund quotes, agency cancellation limits, tour sale prices, and who may change what. See [verification](../../verification/README.md).
