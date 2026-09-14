# Transportation API

**Base path:** `/api/transportations`

| Method | Path | Purpose | Access |
|---|---|---|---|
| `GET` | `/` | Paginated fleet list | Authorized operations staff |
| `GET` | `/search` | Filtered and sorted fleet list | Authorized operations staff |
| `GET` | `/{id}` | Transportation details including seats | Authorized operations staff |
| `POST` | `/` | Create a unit and generate seats | `OWNER`, `MANAGER`, `ADMIN` |
| `PUT` | `/{id}` | Update a unit and optionally apply bulk seat layout | `OWNER`, `MANAGER`, `ADMIN` |
| `PATCH` | `/{id}/status` | Apply a validated unit-status transition | `OWNER`, `MANAGER`, `ADMIN` |
| `POST` | `/imports` | Import multiple units from Excel | `OWNER`, `MANAGER`, `ADMIN` |

## Create request

```json
{
  "transportationNumber": "BHR-1001",
  "code": "BUS-001",
  "type": "BUS",
  "providerName": "Fun Travels",
  "totalCapacity": 40,
  "agencyId": 3,
  "branchId": 7,
  "seatConfig": {
    "PREMIUM_RECLINER": 6,
    "WHEELCHAIR_ACCESSIBLE": 2,
    "KIDS_CHAIR": 4
  }
}
```

List/search responses omit `seats`; the detail response includes seat summaries. This distinction is intentional for performance.
