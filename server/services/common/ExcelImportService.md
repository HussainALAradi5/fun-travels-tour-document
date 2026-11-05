# ExcelImportService

Source: `services/common/ExcelImportService.java`.

Reads spreadsheet uploads (.xlsx, .xls, .csv). The first row is always a header.

## Functions

### `List<List<String>> readRows(MultipartFile file)`

**Purpose:** Data rows as positional cell values, header skipped.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| The file could not be read: | `IllegalArgumentException` | 400 |
| Select a non-empty file. | `IllegalArgumentException` | 400 |
| Import files are limited to   rows. | `IllegalArgumentException` | 400 |

### `List<Map<String, String>> readRowsByHeader(InputStream input)`

**Purpose:** Data rows keyed by normalized header (letters and digits, lower case) plus `#ROW_NUMBER_KEY`.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| The spreadsheet has no header row. | `IllegalArgumentException` | 400 |
| Import files are limited to   rows. | `IllegalArgumentException` | 400 |
