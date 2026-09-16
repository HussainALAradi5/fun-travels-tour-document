# Geography Management Flowcharts

## FC-1: Primary flow

```mermaid
flowchart TD
    A[Geography request] --> B[Manual or sync?]
    B --> C[Validate input/config]
    C --> D{Repository or external API}
    D -- Yes --> E[Map geography data]
    E --> F[Return result]
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


