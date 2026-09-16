# Geography UI Flowcharts

## FC-1: User interaction flow

```mermaid
flowchart TD
    A[Open geography field] --> B[Load options]
    B --> C[Choose country]
    C --> D{Cities load?}
    D -- Yes --> E[Choose city or port]
    D -- No --> X[Submit IDs]
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


