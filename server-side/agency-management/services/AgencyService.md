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

## Detailed behavior and displayed errors

### `getAllAgencies()`

- **What should happen:** Return every persisted agency for trusted administration and legacy consumers. The method must not modify agency data.
- **Processing:** The repository is queried once and its result is returned unchanged.
- **Displayed errors:** No business exception is intentionally raised. An unexpected repository failure must be handled by the global exception handler as a generic request failure; database or Hibernate details must not be shown to the user.

### `searchAgencies(String query, Integer page, Integer size)`

- **What should happen:** Return a bounded, name-ascending page. When `query` is null, empty, or whitespace, the current page of all agencies is returned. Otherwise, only case-insensitive agency-name matches are returned.
- **Processing:** Normalize the search text, construct a validated pageable, execute the appropriate repository query, and map the Spring page to `PageResponse<Agency>`.
- **Business rule:** The searchable selector is server-backed. Empty text means “browse all,” not “show no options.”
- **Displayed errors:** Invalid page or size values use the pagination validation message. Unexpected persistence failures use the generic safe request-failure message.

### `getAgencyById(Integer id)`

- **What should happen:** Return the complete managed agency for the supplied identifier.
- **Processing:** Reject a null identifier, then load the record through the repository.
- **Displayed errors:** A missing agency displays the resource-not-found message for `Agency` and the requested ID. A null ID displays `id must not be null`.

### `createAgencyFromMap(Map<String, Object> payload)`

- **What should happen:** Create one agency, connect valid country/city references, and optionally assign an agency owner. The returned object contains the generated agency ID and resolved relationships.
- **Processing:** Map scalar fields, extract optional relationship IDs, resolve referenced records, save and flush the agency, attach the owner to the saved agency, then persist the owner update in the same transaction.
- **Business rules:** References are resolved to managed entities instead of trusting nested client objects. The owner is linked only after the agency has an ID. Any failure rolls back the complete operation.
- **Displayed errors:** Missing country, city, or owner IDs display the standard resource-not-found message naming that resource and ID. Invalid optional ID text is treated as absent. Validation failures display their field message. Internal mapping or persistence details must not be exposed.

### `getEmployeesByAgencyId(Integer agencyId)`

- **What should happen:** Return only active employees assigned to the agency.
- **Business rule:** Disabled users must not appear in operational employee selectors.
- **Displayed errors:** A null identifier displays `agencyId must not be null`; unexpected repository failures use the generic safe error response.

### `extractId(Map<String, Object> map, String key)`

- **What should happen:** Convert a numeric or numeric-text payload field to `Integer`; return `null` when missing or invalid.
- **Business rule:** This helper makes optional relationship fields tolerant, but required relationship validation still belongs to the calling workflow.
- **Displayed errors:** None. It is private and never directly produces an API response.
