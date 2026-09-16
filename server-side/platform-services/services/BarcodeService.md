# Barcode Service

**Source:** `src/main/java/com/server/server/services/BarcodeService.java`

## Function reference

| Function | Signature | Parameters | Function logic | Business logic | Return value | Side effects | Exceptions |
|---|---|---|---|---|---|---|---|
| `generateQRCodeBase64` | `public String generateQRCodeBase64(String text)` | `text`: required QR payload | Delegates to `generateBase64` with QR format and 300×300 dimensions. | Produces a portable ticket/reference code. | Raw Base64 PNG text. | Allocates an in-memory image. | Propagates `"Error generating barcode/QR"`. |
| `generateBarcodeBase64` | `public String generateBarcodeBase64(String text)` | `text`: required barcode payload | Delegates with Code 128 and 400×100 dimensions. | Provides scanner-compatible linear codes. | Raw Base64 PNG text. | Allocates an in-memory image. | Propagates `"Error generating barcode/QR"`. |
| `generateBase64` | `private String generateBase64(String text, BarcodeFormat format, int width, int height)` | Payload, format, positive dimensions | Encodes a bit matrix, writes PNG bytes, then Base64-encodes them. | Centralizes identical generation behavior. | Raw Base64 image. | None outside memory. | `RuntimeException`: `"Error generating barcode/QR"`. |
| `readBarcodeFromBase64` | `public String readBarcodeFromBase64(String base64Image)` | Raw Base64 or data URI | Removes a data-URI prefix, decodes the image, auto-detects its barcode format, and reads the payload. | Accepts browser-provided images without client preprocessing. | Decoded barcode text. | None. | `RuntimeException`: `"Could not decode the provided image. Ensure the QR/Barcode is clearly visible."` |

All functions are stateless and have no direct authorization or database transaction.

## Expected behavior and displayed errors

- `generateQRCodeBase64` should return a raw Base64 PNG representing the exact supplied text at 300 x 300 pixels.
- `generateBarcodeBase64` should return a Code 128 PNG at 400 x 100 pixels.
- `generateBase64` is the shared implementation: encode, render to PNG in memory, then Base64-encode. It never writes a file.
- `readBarcodeFromBase64` should accept raw Base64 and browser data URIs, remove the optional prefix, decode the image, and return its embedded text.

Generation failures display `Error generating barcode/QR`. An unreadable, corrupt, or unsupported image displays `Could not decode the provided image. Ensure the QR/Barcode is clearly visible.` The response must not include ZXing stack traces or image-library internals.
