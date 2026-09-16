# Support and Tracking Management Flowcharts

## FC-1: Primary flow

```mermaid
flowchart TD
    A[Support action] --> B[Authorize participant]
    B --> C[Request open?]
    C --> D{Apply transition/comment}
    D -- Yes --> E[Log event + notify]
    E --> F[Return timeline]
    D -- No --> X[Return clear error]
```

## FC-2: Failure handling

```mermaid
flowchart LR
    R[Request] --> V{Validation and authorization}
    V -- Invalid --> E[ApiResponse error]
    V -- Valid --> T[Transactional operation]
    T -->|Failure| B[Rollback]
    B --> E
    T -->|Success| S[Response and audit/notification]
```


