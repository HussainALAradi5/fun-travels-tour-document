# Transportation

Table `transportations`. Inherits `BaseEntity`. Source: `models/tourmanagement/Transportation.java`.

| Field | Type | Notes |
| --- | --- | --- |
| `transportationNumber` | `String` |  unique, required |
| `tours` | `List<Tour>` | OneToMany  |
| `type` | `TransportationType` |  required |
| `providerName` | `String` |   |
| `status` | `GenericStatus` |  required |
| `totalCapacity` | `Integer` |  required |
| `unitStatus` | `TransportationStatus` |  required |
| `agency` | `Agency` | ManyToOne  |
| `agencyBranch` | `AgencyBranch` | ManyToOne  |
| `seats` | `List<Seat>` | OneToMany  |
| `seatConfig` | `java.util.Map<String, Integer>` |  not stored |
