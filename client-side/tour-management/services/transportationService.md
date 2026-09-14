# Transportation API Client

**Source:** `src/Api/tourmanagement/Transportation.ts`

| Method | Result | Purpose |
|---|---|---|
| `getAll(params)` | `PageResponse<Transportation>` | Paginated fleet list |
| `search(params)` | `PageResponse<Transportation>` | Search, filter, date/sort pagination parameters |
| `getById(id)` | `Transportation` | Detail including seat summaries |
| `create(request)` | `Transportation` | Create a unit and seat layout |
| `update(id, data)` | `Transportation` | Update details or bulk seat configuration |
| `updateStatus(id, status)` | `Transportation` | Change operational status |
| `importExcel(file)` | `ImportResult` | Server-side spreadsheet import |

The import client sends `multipart/form-data`; spreadsheet parsing and business validation remain on the backend.
