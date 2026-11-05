## Business logic

`getVisible` (the public `GET /api/tours/{id}`): ACTIVE (bookable) tours are public; other tours are shown to administrators, the owning agency's staff, and customers holding a ticket for the tour. Anyone else gets 404, so pending or cancelled tours do not leak.

`getAll` and `filter` list every tour for administrators, the agency's tours for agency staff (managers and employees also only their branch's), and only ACTIVE tours for everyone else. `getCatalogTours` is the public catalog: bookable tours by start/end country and date range.
