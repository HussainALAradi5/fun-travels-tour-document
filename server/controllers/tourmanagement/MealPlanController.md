# MealPlanController

Base path `/api/meals`. Source: `controllers/tourmanagement/MealPlanController.java`.

Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, 401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.

| Method and path | Service function | Why it is used | Role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `GET /api/meals` | - | Get all meals. | public | query `page`, `size`, `sortDir` | `PageResponse<MealPlanResponse>` |
| `GET /api/meals/agency/{agencyId}` | - | Get menu. | public | query `page`, `size` | `PageResponse<MealPlanResponse>` |
| `POST /api/meals` | - | Define meal. | OWNER, MANAGER, ADMIN | body `MealPlanCreateRequest` | `MealPlanResponse` |
| `PATCH /api/meals/{id}/status` | - | Toggle status. | OWNER, MANAGER, ADMIN | query `status` | `Void` |
| `PUT /api/meals/{id}/price` | - | Update price. | OWNER, MANAGER, ADMIN | query `price` | `MealPlanResponse` |
