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
