# Tour, Booking, Ticket, and Inventory Management Flowcharts

## FC-1: Primary flow

```mermaid
flowchart TD
    A[Tour selected] --> B[Validate booking]
    B --> C[Lock capacity + seats]
    C --> D{Create 15-minute hold}
    D -- Yes --> E[Payment completed?]
    E --> F[Confirm booking]
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


