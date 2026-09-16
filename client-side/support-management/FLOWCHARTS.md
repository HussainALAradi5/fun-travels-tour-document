# Support UI Flowcharts

## FC-1: User interaction flow

```mermaid
flowchart TD
    A[Open support] --> B[Load scoped data]
    B --> C[Choose action]
    C --> D{Action allowed?}
    D -- Yes --> E[Submit and refresh]
    D -- No --> X[Show workflow error]
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


