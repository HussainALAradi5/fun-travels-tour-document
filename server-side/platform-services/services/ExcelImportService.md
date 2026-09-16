# Generic Excel and CSV Import Service

**Source:** `src/main/java/com/server/server/services/ExcelImportService.java`

## Function reference

| Function | Signature | Parameters | Function logic | Business logic | Return value | Exceptions |
|---|---|---|---|---|---|---|
| `importFile` | `public <T> List<T> importFile(MultipartFile file, Supplier<T> entitySupplier, BiConsumer<T,List<String>> mapper)` | Uploaded file, entity constructor, row mapper | Selects CSV when the filename ends in `.csv`; otherwise selects Excel parsing. | Gives feature imports one reusable file-to-entity pipeline. | Mapped entity list. | Propagates format-specific wrapped failures. |
| `importExcel` | `private <T> List<T> importExcel(MultipartFile file, Supplier<T> entitySupplier, BiConsumer<T,List<String>> mapper)` | Same inputs | Opens the first sheet, skips row zero, ignores empty rows, extracts cells, creates entities, and maps columns. | Spreadsheet headers are metadata, not records. | Mapped entity list. | `RuntimeException`: `"Excel processing failed: {reason}"`. |
| `importCsv` | `private <T> List<T> importCsv(MultipartFile file, Supplier<T> entitySupplier, BiConsumer<T,List<String>> mapper)` | Same inputs | Reads UTF-8, skips the header, ignores blank lines, respects quoted commas, strips quotes, creates entities, and maps columns. | CSV import matches the Excel row abstraction. | Mapped entity list. | `RuntimeException`: `"CSV processing failed: {reason}"`. |
| `getSafeCellValue` | `public String getSafeCellValue(Row row, int cellIndex)` | Row and zero-based index | Converts string, numeric, date, boolean, and formula cells to safe text; unsupported/missing cells become empty strings. | Normalizes Apache POI values before domain mapping. | Cell text. | Formula string lookup falls back to numeric lookup; conversion errors may propagate. |
| `isRowEmpty` | `private boolean isRowEmpty(Row row)` | Excel row | Scans its used range for any nonblank cell. | Prevents empty records from reaching business validation. | Boolean. | None directly. |

The generic importer only parses and maps. Feature services remain responsible for validation, authorization, persistence, and row-level business messages.

## Expected behavior and displayed errors

### `importFile(...)`

Determines the parser from the uploaded filename, delegates row conversion through the supplied mapper, and returns mapped entities without persisting them. CSV names use the CSV parser; other supported spreadsheet uploads use the Excel parser. Feature code must validate file type and size before calling this generic layer.

### `importExcel(...)`

Reads the first worksheet, treats row zero as a header, ignores fully blank rows, converts each remaining row to normalized strings, and invokes the domain mapper once per data row. A processing failure displays `Excel processing failed: {reason}` to administrative users; low-level library/stack details must be logged rather than returned.

### `importCsv(...)`

Reads UTF-8 text, skips the first/header line, ignores blank lines, preserves commas inside quoted values, and maps each data row. A processing failure displays `CSV processing failed: {reason}`. Domain validation should add a row number and business explanation when it converts this generic error into an import result.

### `getSafeCellValue(...)` and `isRowEmpty(...)`

These helpers normalize missing, text, numeric, date, boolean, and formula cells and prevent blank records. They do not create user responses directly. Any conversion error is attributed to the current import row by the calling feature service.
