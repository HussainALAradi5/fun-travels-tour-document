# Tour, Booking, Ticket, and Inventory UI Flowcharts

## FC-1: User interaction flow

```mermaid
flowchart TD
    A[Open tour feature] --> B[Load typed options]
    B --> C[Complete guided form]
    C --> D{API succeeds?}
    D -- Yes --> E[Refresh state]
    D -- No --> X[Show actionable error]
```

## FC-2: API state flow

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Loading: request
    Loading --> Success: API success
    Loading --> Error: safe API error
    Error --> Loading: retry
    Success --> Loading: refresh or mutation
```


