# ExcelImportService

Source: `services/common/ExcelImportService.java`.

Reads spreadsheet uploads (.xlsx, .xls, .csv). The first row is always a header.

## Functions

### `List<List<String>> readRows(MultipartFile file)`

**Purpose:** Data rows as positional cell values, header skipped.

### `List<Map<String, String>> readRowsByHeader(InputStream input)`

**Purpose:** Data rows keyed by normalized header (letters and digits, lower case) plus `#ROW_NUMBER_KEY`.
