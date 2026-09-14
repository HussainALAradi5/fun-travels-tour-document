# Agency API

**Base path:** `/api/agencies`

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/` | Return the existing non-paginated agency list for legacy screens |
| `GET` | `/search` | Return paginated agency options, with optional name query |
| `GET` | `/{id}` | Return one agency |
| `GET` | `/{id}/employees` | Return active agency employees |
| `POST` | `/` | Create an agency and resolve its country, city, and owner |

## Search parameters

| Parameter | Default | Description |
|---|---:|---|
| `query` | empty | Case-insensitive agency-name search; empty returns the normal paginated list |
| `page` | `0` | Zero-based page |
| `size` | `20` | Page size, capped by shared pagination rules |

Numeric route constraints prevent `/search` from being interpreted as an agency ID.
