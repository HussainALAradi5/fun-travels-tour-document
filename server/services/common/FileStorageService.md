# FileStorageService

Source: `services/common/FileStorageService.java`.

Stores validated uploads under `app.upload-dir`. Only JPEG and PNG images are accepted.

## Functions

### `String saveProfileImage(String base64Data, Integer userId)`

**Purpose:** Saves the image as `profiles/user_<id>.<ext>` and returns its public path.
