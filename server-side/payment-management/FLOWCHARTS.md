# Payment and Wallet Management Flowcharts

## FC-1: Primary flow

```mermaid
flowchart TD
    A[Payment request] --> B[Validate payable state]
    B --> C[Completed payment exists?]
    C --> D{Execute method}
    D -- Yes --> E[Persist payment + ledger]
    E --> F[Confirm reservation]
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


