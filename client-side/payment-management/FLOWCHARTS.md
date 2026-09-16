# Payment and Wallet UI Flowcharts

## FC-1: User interaction flow

```mermaid
flowchart TD
    A[Open payment] --> B[Validate input]
    B --> C[Submit once]
    C --> D{Payment succeeds?}
    D -- Yes --> E[Refresh state]
    D -- No --> X[Show safe error]
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


