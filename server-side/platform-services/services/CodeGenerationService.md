# Code Generation Service

**Source:** `src/main/java/com/server/server/services/CodeGenerationService.java`

## Function reference

| Function | Signature | Parameters | Function logic | Business logic | Return value | Side effects | Exceptions |
|---|---|---|---|---|---|---|---|
| `generateQRCode` | `public String generateQRCode(String text, int width, int height) throws Exception` | Payload and output dimensions | Generates a QR bit matrix and converts it to PNG Base64. | Embeds verifiable ticket identity. | Browser-ready data URI. | In-memory encoding. | Propagates ZXing/image-writing exceptions. |
| `generateBarcode` | `public String generateBarcode(String text, int width, int height) throws Exception` | Payload and output dimensions | Generates Code 128 and converts it to PNG Base64. | Supports conventional ticket scanners. | Browser-ready data URI. | In-memory encoding. | Propagates ZXing/image-writing exceptions. |
| `convertToBase64` | `private String convertToBase64(BitMatrix bitMatrix) throws Exception` | Generated matrix | Writes PNG bytes and prefixes encoded content with `data:image/png;base64,`. | Allows direct use in an HTML `img` source. | PNG data URI. | In-memory stream creation. | Propagates image-writing exceptions. |

The caller translates technical generation failures into customer-readable workflow messages.
