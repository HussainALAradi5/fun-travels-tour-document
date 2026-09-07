# Agency DTOs

## AgencyCreateRequest

```java
public class AgencyCreateRequest {
    private String agencyName;
    private String address;
    private String contactNumber;
    private String ownerMobileNumber;
    private Integer countryId;
    private Integer cityId;
    private Integer agencyOwnerId;
}
```

## AgencyResponse

```java
public class AgencyResponse {
    private Integer id;
    private String agencyName;
    private String address;
    private String contactNumber;
    private String ownerMobileNumber;
    private CountrySummary country;
    private CitySummary city;
    private UserSummary agencyOwner;
    private boolean active;
    private List<AgencyBranchSummary> branches;
}
```

## AgencyBranchCreateRequest

```java
public class AgencyBranchCreateRequest {
    private String branchName;
    private String branchAddress;
    private String contactNumber;
    private String ownerMobileNumber;
    private Integer agencyId;
    private Integer countryId;
    private Integer cityId;
    private Integer branchManagerId;
}
```

## AgencyBranchResponse

```java
public class AgencyBranchResponse {
    private Integer id;
    private String branchName;
    private String branchAddress;
    private String contactNumber;
    private AgencySummary agency;
    private CountrySummary country;
    private CitySummary city;
    private UserSummary branchManager;
    private boolean active;
    private int employeeCount;
}
```
