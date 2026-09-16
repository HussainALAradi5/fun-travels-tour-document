# Agency Management UI Flowcharts

## FC-1: User interaction flow

```mermaid
flowchart TD
    A[Open selector] --> B[Request page]
    B --> C[Search typed?]
    C --> D{API succeeds?}
    D -- Yes --> E[Render options]
    D -- No --> X[Select or deselect]
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


