# File Storage Service

**Source:** `src/main/java/com/server/server/services/FileStorageService.java`

## `saveBase64Image`

**Signature:** `public String saveBase64Image(String base64Data, String preferredName)`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `base64Data` | `String` | Yes | Raw Base64 or data-URI image. |
| `preferredName` | `String` | Yes | Stable filename stem. |

**Function logic:** Creates `uploads/profiles`, strips an optional data-URI prefix, decodes bytes, writes `{preferredName}.jpg`, and returns its public path.

**Business logic:** Profile updates need a stable URL and replace the prior image for the same preferred name.

**Return value:** `/uploads/profiles/{preferredName}.jpg`.

**Side effects:** Creates directories and writes or overwrites a local file.

**Exception:** `RuntimeException` with `"Could not save image file: {reason}"` for filesystem I/O failures. Invalid Base64 may propagate `IllegalArgumentException`.

**Authorization and transaction:** Authorization belongs to the calling profile workflow; no database transaction.
