## Business logic

- `issue` builds one unsaved ticket per traveler selection with a `TKT-` number, QR code (`TICKET|TOUR|CUSTOMER` payload), and Code 128 barcode.
- Meals must be offered by the tour, ACTIVE, and not selected twice for the same traveler.
- `applyPricing` = (tour price - 50% kids-chair discount) + seat price modifier + selected meal prices, never below zero (`PricingCalculator.ticketPrice`). It runs again after seats are auto-assigned so the assigned seat's modifier and discount apply.
