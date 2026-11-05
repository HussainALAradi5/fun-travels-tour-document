# MealPlanController

Base path `/api/v1/meals`. Source: `controllers/tourmanagement/MealPlanController.java`.

Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it calls; each service page lists the cases behind them.

| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |
| --- | --- | --- | --- | --- | --- | --- |
| `GET /api/v1/meals` | - | Get all meals. | public | query `page`, `size`, `sortDir` | `PageResponse<MealPlanResponse>` | 400 |
| `GET /api/v1/meals/agency/{agencyId}` | - | Get menu. | public | query `page`, `size` | `PageResponse<MealPlanResponse>` | 400 |
| `POST /api/v1/meals` | - | Define meal. | OWNER, MANAGER, ADMIN | body `MealPlanCreateRequest` | `MealPlanResponse` | 400, 401, 403 |
| `PUT /api/v1/meals/{id}` | - | Update meal. | OWNER, MANAGER, ADMIN | body `MealPlanCreateRequest` | `MealPlanResponse` | 400, 401, 403 |
| `PATCH /api/v1/meals/{id}/status` | - | Toggle status. | OWNER, MANAGER, ADMIN | query `status` | `Void` | 400, 401, 403 |
