## Business logic

Loads report rows through the same service methods the list pages use, so every scoping rule applies unchanged: customers see their own tickets and transactions, agency staff their own agency's tours, vehicles, meals, tickets, and staff. Paged sources are read page by page (100 per page) up to `ReportRules.MAX_ROWS` (5000); larger reports are cut and say so. The passenger manifest needs `tourId` and access to the tour's agency; agency branches and employees need `agencyId` and access to that agency. Runs in one read-only transaction and returns plain values (`ReportTable`).
