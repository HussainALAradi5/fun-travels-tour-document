# User DTOs

Data Transfer Objects for User Management.

## LoginRequest

```java
public class LoginRequest {
    private String identifier;  // email, username, or mobile
    private String password;
}
```

## RegisterRequest

```java
public class RegisterRequest {
    private String userName;
    private String name;
    private String email;
    private String password;
    private String mobileNumber;
    private Integer age;
}
```

## AuthResponse

```java
public class AuthResponse {
    private String token;
    private User user;
}
```

## PasswordResetRequest

```java
public class PasswordResetRequest {
    private String email;
    private String baseNumber;
}
```

## PasswordResetConfirm

```java
public class PasswordResetConfirm {
    private String identifier;
    private String baseNumber;
    private String token;
    private String newPassword;
}
```

## UserResponse

```java
public class UserResponse {
    private Integer id;
    private String userName;
    private String name;
    private String email;
    private String mobileNumber;
    private Integer age;
    private UserTypeEnum userType;
    private String profileImageUrl;
    private boolean active;
    private AgencySummary agency;
    private AgencyBranchSummary agencyBranch;
}
```

## UserUpdateRequest

```java
public class UserUpdateRequest {
    private String name;
    private String mobileNumber;
    private Integer age;
    private String profileImageUrl;
    private String base64Image;
}
```

## BulkImportResponse

```java
public class BulkImportResponse {
    private int imported;
    private int skipped;
    private List<User> users;
}
```
