# Support Management DTOs

## UserRequestCreateRequest

```java
public class UserRequestCreateRequest {
    private String subject;
    private String description;
    private UserRequestType requestType; // SUPPORT or SUGGESTION
}
```

## UserRequestResponse

```java
public class UserRequestResponse {
    private Integer id;
    private String subject;
    private String description;
    private UserRequestType requestType;
    private UserRequestStatus status;
    private String resolution;
    private UserSummary submitter;
    private UserSummary assignedTo;
    private UserSummary solvedBy;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
```

## AssignAgentRequest

```java
public class AssignAgentRequest {
    private Integer agentId;
}
```

## SolveRequest

```java
public class SolveRequest {
    private String resolution;
}
```

## RejectRequest

```java
public class RejectRequest {
    private String reason;
}
```

## CommentCreateRequest

```java
public class CommentCreateRequest {
    private String referenceType; // TOUR, RESERVATION, TICKET, USER, USER_REQUEST
    private Integer referenceId;
    private String content;
}
```

## CommentResponse

```java
public class CommentResponse {
    private Integer id;
    private String referenceType;
    private Integer referenceId;
    private String content;
    private UserSummary author;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
```

## EventLogResponse

```java
public class EventLogResponse {
    private Integer id;
    private String referenceType;
    private Integer referenceId;
    private String eventType;
    private String description;
    private UserSummary actor;
    private LocalDateTime createdAt;
}
```

## TimelineItem

```java
public class TimelineItem {
    private String type; // "COMMENT" or "EVENT"
    private LocalDateTime timestamp;
    private Object data; // CommentResponse or EventLogResponse
}
```
