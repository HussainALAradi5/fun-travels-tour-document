# Country

Table `countries`. Inherits `BaseEntity`. Source: `models/geography/Country.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `famousName` | `String` |  required |
| `officialName` | `String` |   |
| `countryCode` | `String` |  unique |
| `dialCode` | `String` |   |
| `mobileNumberLength` | `Integer` |   |
| `flagPngUrl` | `String` |   |
| `flagSvgUrl` | `String` |   |
