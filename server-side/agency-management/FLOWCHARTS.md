# Agency Management Flowcharts

## FC-1: Primary flow

```mermaid
flowchart TD
    A[Request] --> B[Authorize role]
    B --> C[Validate references]
    C --> D{Ownership / uniqueness valid?}
    D -- Yes --> E[Persist agency data]
    E --> F[Return response]
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


