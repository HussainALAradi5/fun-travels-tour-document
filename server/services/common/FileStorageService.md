# FileStorageService

Source: `services/common/FileStorageService.java`.

Stores files. Profile images go to the public `app.upload-dir` (JPEG and PNG only); private files such as reports go to `app.media-dir`, which is only reachable through access-checked endpoints.

## Functions

### `String replaceProfileImage(String base64Data, Integer userId, String previousPath)`

**Purpose:** Saves the image under a new name (`profiles/user_<id>_<millis>.<ext>`) so browsers never show a cached old picture, deletes the previous file, and returns the new public path.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Images must be at most   KB. | `IllegalArgumentException` | 400 |
| Only JPEG and PNG images are supported. | `IllegalArgumentException` | 400 |
| Could not save image file. | `StorageException` | 500 |
| The image data is not valid base64. | `IllegalArgumentException` | 400 |

### `void deleteProfileImage(String publicPath)`

**Purpose:** Deletes a stored profile image by its public path; paths outside the profile folder are ignored.

**Exceptions:** none of its own; failures come from the functions it calls.

### `void writePrivate(String relativePath, byte[] content)`

**Purpose:** Writes a private file (relative to `app.media-dir`); private files are never served statically.

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Could not save the file. | `StorageException` | 500 |
| Invalid file path. | `IllegalArgumentException` | 400 |

### `byte[] readPrivate(String relativePath)`

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| The stored file is missing. | `StorageException` | 500 |
| Invalid file path. | `IllegalArgumentException` | 400 |

### `void deletePrivate(String relativePath)`

**Cases and exceptions:**

| Case | Exception | Status |
| --- | --- | --- |
| Invalid file path. | `IllegalArgumentException` | 400 |
