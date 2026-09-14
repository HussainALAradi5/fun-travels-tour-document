# Agency Service

**Source:** `src/main/java/com/server/server/services/agency/AgencyService.java`

## Function reference

| Function and signature | Parameters | Function logic | Business logic | Return and side effects | Exceptions / authorization |
|---|---|---|---|---|---|
| `public List<Agency> getAllAgencies()` | None | Calls `findAll`. | Supports complete-list legacy/internal consumers. | All agencies; read-only. | None directly. |
| `public PageResponse<Agency> searchAgencies(String query, Integer page, Integer size)` | Optional search and pagination | Trims search, creates name-ascending pageable, uses `findAll` when blank or case-insensitive name search otherwise. | Remote selectors must show all page results before typing and remain server-paginated. | One agency page; read-only. | Pagination validation may propagate. |
| `public Agency getAgencyById(Integer id)` | Required agency ID | Null-checks and queries by ID. | Every agency reference must resolve to a real owner aggregate. | Agency; read-only. | `ResourceNotFoundException("Agency", id)`; null produces `"id must not be null"`. |
| `public Agency createAgencyFromMap(Map<String,Object> payload)` | Agency fields plus optional `countryId`, `cityId`, `agencyOwnerId` | Maps payload, resolves geography, saves/flushed agency, resolves owner, links both sides, and saves owner. | Relationships use managed entities; flush creates the agency ID before owner linkage. | Created agency; writes agency and optional owner. | Resource-standard messages for missing country, city, or user. |
| `public List<User> getEmployeesByAgencyId(Integer agencyId)` | Required agency ID | Queries active users by agency. | Deactivated accounts are excluded. | Active employee list; read-only. | Null produces `"agencyId must not be null"`. |
| `private Integer extractId(Map<String,Object> map, String key)` | Payload and property name | Returns parsed integer; missing or invalid text becomes `null`. | Optional relationship IDs do not break payload mapping. | ID or `null`; no side effects. | None directly. |

Read functions use `@Transactional(readOnly = true)`; creation uses `@Transactional`.
