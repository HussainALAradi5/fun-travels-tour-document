# Notification Management Flowcharts

## FC-1: Primary flow

```mermaid
flowchart TD
    A[Domain event / query] --> B[Resolve recipient]
    B --> C[Build or filter notification]
    C --> D{Persist / query}
    D -- Yes --> E[Map response]
    E --> F[Deliver result]
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


