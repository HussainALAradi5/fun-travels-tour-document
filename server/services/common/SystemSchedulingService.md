# SystemSchedulingService

Source: `services/common/SystemSchedulingService.java`.

## Functions

### `void registerNightlyTask(Runnable task)`

**Purpose:** Other services call this to register their cleanup logic.

### `void runNightlyMaintenance()`

**Runs in:** scheduled `cron = "0 0 0 * * *"`
