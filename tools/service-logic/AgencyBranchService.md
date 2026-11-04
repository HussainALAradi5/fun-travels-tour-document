## Business logic

- Listing, searching, and the branch staff list are for administrators and the agency's own staff.
- `addBranch`: owners add branches to their own agency, admins to any; names are unique per agency. The optional manager must have the MANAGER role and be unassigned or already in this agency; a manager of another agency is never moved over.
