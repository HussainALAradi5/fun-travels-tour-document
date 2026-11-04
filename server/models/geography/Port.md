# Port

Table `ports`. Inherits `BaseEntity`. Source: `models/geography/Port.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `portName` | `String` |  required |
| `portCode` | `String` |  unique |
| `portType` | `PortType` |  required |
| `city` | `City` | ManyToOne  |
| `country` | `Country` | ManyToOne  |
| `latitude` | `Double` |   |
| `longitude` | `Double` |   |
| `status` | `GenericStatus` |  required |
