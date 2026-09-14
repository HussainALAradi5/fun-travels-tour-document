# Reusable UI Components

The component library is built with Chakra UI and typed TypeScript interfaces. Components support responsive layouts and both light and dark color modes.

## Forms and selection

- `DynamicForm` renders typed `FieldConfig` definitions, supports nested paths such as `seatConfig.KIDS_CHAIR`, and memoizes fields for responsive typing.
- `FormSelect` renders local options with optional Lucide icons.
- `PaginatedSearchSelect` supports local options or a debounced backend loader returning `PageResponse<SelectOption>`.
- `FormCombobox` is the thin adapter between `DynamicForm` and `PaginatedSearchSelect`.
- `DatePicker` supports single/range selection, deterministic SSR, accessible controls, and valid HTML nesting.

## Dialogs

- `AppDialog` provides the shared accessible dialog surface.
- `DynamicFormDialog` hosts configuration-driven forms.
- `GuidedStepsDialog` renders reusable step-by-step instructions.
- `ExcelImportDialog` handles file selection, submission state, and row-result feedback.
- `ConfirmDialog`, `DataTableDialog`, and `ExportDialog` cover common operational workflows.

## Pagination and filtering

The UI consumes the shared `PageResponse<T>` contract. Sort direction uses the dedicated `SortDirection` type. Date and domain filter interfaces remain separate from pagination metadata, allowing service and endpoint contracts to stay precise.

## Reliability

- Root rendering suppresses only unavoidable theme/extension attribute differences.
- Time-dependent UI uses `useIsHydrated` where necessary.
- Browser listeners are registered in effects and cleaned up.
- Axios errors are translated into customer-readable messages.
- Dialogs avoid nested interactive HTML and conflicting modal focus scopes.
