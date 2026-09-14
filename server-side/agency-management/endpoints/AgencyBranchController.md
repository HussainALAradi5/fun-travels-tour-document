# Agency Branch API

**Base path:** `/api/branches`

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/` | Return all branches for legacy screens |
| `GET` | `/agency/{agencyId}` | Return active branches for an agency |
| `GET` | `/agency/{agencyId}/search` | Paginated branch selection/search |
| `POST` | `/agency/{agencyId}` | Create a branch under an agency |
| `GET` | `/agency/{agencyId}/branch/{branchId}/employees` | Return branch employees after ownership validation |

An empty `query` returns the agency's paginated branch list. A non-empty value performs a case-insensitive branch-name search. All identifier path variables are constrained to numeric values.
