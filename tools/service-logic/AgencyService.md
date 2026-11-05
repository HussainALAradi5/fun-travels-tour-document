## Business logic

- `getAllAgencies` and `searchAgencies`: administrators see every agency; agency staff only their own; other roles are refused for search.
- `getVisibleAgency` (the `GET /api/agencies/{id}` endpoint) and `getEmployeesByAgencyId`: administrators and the agency's own staff only, because the response holds the owner's and staff members' contacts.
- `createAgency` (admin): city must belong to the country, names are unique per country, and the optional owner must have the OWNER role.
