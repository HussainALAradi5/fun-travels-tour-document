# System Scheduling Service

**Source:** `src/main/java/com/server/server/services/SystemSchedulingService.java`

## Function reference

| Function | Signature | Parameters | Function logic | Business logic | Return/side effects | Exceptions and transaction |
|---|---|---|---|---|---|---|
| `registerNightlyTask` | `public void registerNightlyTask(Runnable task)` | `task`: required maintenance callback | Appends the callback to the in-memory task list. | Lets feature services register cleanup without duplicating scheduler configuration. | Mutates the task registry. | No explicit exception or transaction. |
| `runNightlyMaintenance` | `public void runNightlyMaintenance()` | None | At midnight, logs the count, runs every callback independently, logs individual failures, then completion. | One failed maintenance task must not prevent the remaining tasks. | Runs all registered jobs. | Catches each exception and logs `"Scheduled task failed: {reason}"`; no transaction is imposed across tasks. |

## Expected behavior and failure handling

### `registerNightlyTask(Runnable task)`

Adds a feature-owned maintenance callback to the in-memory registry. Registration should happen once during application startup. The callback must be safe to run repeatedly because a restarted or retried scheduler may execute maintenance again. This method has no browser-facing result.

### `runNightlyMaintenance()`

At the configured midnight schedule, logs how many tasks will run, executes every registered callback independently, records each failure as `Scheduled task failed: {reason}`, and continues with the remaining callbacks. There is deliberately no transaction spanning every task: each feature owns its transaction boundary.

Scheduled failures are operational, not customer-facing. They should appear in structured server logs and monitoring with the task identity. No raw scheduling error should be displayed in an unrelated user request. Repeated failures should trigger an operational alert in a production deployment.
