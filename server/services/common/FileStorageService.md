# FileStorageService

Source: `services/common/FileStorageService.java`.

Stores files. Profile images go to the public `app.upload-dir` (JPEG and PNG only); private files such as reports go to `app.media-dir`, which is only reachable through access-checked endpoints.

## Functions

### `String replaceProfileImage(String base64Data, Integer userId, String previousPath)`

**Purpose:** Saves the image under a new name (`profiles/user_<id>_<millis>.<ext>`) so browsers never show a cached old picture, deletes the previous file, and returns the new public path.

### `void deleteProfileImage(String publicPath)`

**Purpose:** Deletes a stored profile image by its public path; paths outside the profile folder are ignored.

### `void writePrivate(String relativePath, byte[] content)`

**Purpose:** Writes a private file (relative to `app.media-dir`); private files are never served statically.

### `byte[] readPrivate(String relativePath)`

### `void deletePrivate(String relativePath)`
