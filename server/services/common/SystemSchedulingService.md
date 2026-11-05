# SystemSchedulingService

Source: `services/common/SystemSchedulingService.java`.

Runs the nightly jobs other services register. Services register `this::method`, which bypasses their transactional proxy, so each job runs here in its own transaction: one failing job rolls back only itself.

## Functions

### `void registerNightlyTask(Runnable task)`

**Exceptions:** none of its own; failures come from the functions it calls.

### `void runNightlyMaintenance()`

**Runs in:** scheduled `cron = "0 0 0 * * *"`

**Exceptions:** none of its own; failures come from the functions it calls.
