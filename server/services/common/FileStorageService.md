# FileStorageService

Source: `services/common/FileStorageService.java`.

Stores validated uploads under `app.upload-dir`. Only JPEG and PNG images are accepted.

## Functions

### `String replaceProfileImage(String base64Data, Integer userId, String previousPath)`

**Purpose:** Saves the image under a new name (`profiles/user_<id>_<millis>.<ext>`) so browsers never show a cached old picture, deletes the previous file, and returns the new public path.

### `void deleteProfileImage(String publicPath)`

**Purpose:** Deletes a stored profile image by its public path; paths outside the profile folder are ignored.
