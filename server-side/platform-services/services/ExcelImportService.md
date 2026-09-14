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
