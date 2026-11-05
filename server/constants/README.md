# Constants

Shared values live in `constants/`; services never repeat them inline.

## BookingRules

| Name | Value |
| --- | --- |
| `HOLD_MINUTES` | `15` |
| `FULL_REFUND_AFTER_DAYS` | `14` |
| `HALF_REFUND_MIN_DAYS` | `7` |
| `HALF_REFUND_RATE` | `new BigDecimal("0.50")` |
| `KIDS_CHAIR_DISCOUNT_RATE` | `new BigDecimal("0.50")` |
| `TOUR_CANCELLATION_MIN_DAYS` | `14` |
| `TOUR_CANCELLATION_MAX_BOOKED_RATIO` | `1.0 / 3.0` |
| `REMINDER_DAYS_BEFORE_TOUR` | `7` |
| `PASSWORD_RESET_MINUTES` | `15` |
| `MIN_PASSWORD_LENGTH` | `6` |
| `QR_SIZE` | `250` |
| `BARCODE_WIDTH` | `300` |
| `BARCODE_HEIGHT` | `100` |
| `CURRENCY` | `"USD"` |

## CodePrefixes

| Name | Value |
| --- | --- |
| `TICKET` | `"TKT"` |
| `RESERVATION` | `"RES"` |
| `PAYMENT` | `"TRX"` |
| `ACCOUNT` | `"ACC"` |

## ReportRules

| Name | Value |
| --- | --- |
| `MAX_ROWS` | `5000` |
| `LOAD_PAGE_SIZE` | `100` |
| `BRAND_NAME` | `"Fun Travels Tour"` |
| `BRAND_TAGLINE` | `"Travel agency management platform"` |
| `CONFIDENTIALITY` | `"Confidential - for internal use only"` |
| `MEDIA_REPORT_FOLDER` | `"reports"` |

## RoleGroups

| Name | Value |
| --- | --- |
| `AGENCY_STAFF` | `EnumSet.of( UserTypeEnum.OWNER, UserTypeEnum.MANAGER, UserTypeEnum.EMPLOYEE)` |
| `BRANCH_STAFF` | `EnumSet.of(UserTypeEnum.MANAGER, UserTypeEnum.EMPLOYEE)` |
| `SUPPORT_STAFF` | `EnumSet.of( UserTypeEnum.ADMIN, UserTypeEnum.SUPPORT_AGENT)` |
| `OWNER_CREATABLE` | `EnumSet.of( UserTypeEnum.MANAGER, UserTypeEnum.EMPLOYEE)` |
| `MANAGER_CREATABLE` | `EnumSet.of(UserTypeEnum.EMPLOYEE)` |
| `REPORT_STAFF` | `EnumSet.of( UserTypeEnum.ADMIN, UserTypeEnum.OWNER, UserTypeEnum.MANAGER, UserTypeEnum.EMPLOYEE)` |
| `USER_REPORT` | `EnumSet.of(UserTypeEnum.ADMIN, UserTypeEnum.MANAGER)` |
| `IMPORTABLE` | `EnumSet.of( UserTypeEnum.MANAGER, UserTypeEnum.EMPLOYEE)` |

## ValidationPatterns

| Name | Value |
| --- | --- |
| `MOBILE_NUMBER` | `"^\\+[1-9]\\d{7,14}$"` |
| `MOBILE_NUMBER_MESSAGE` | `"Mobile number must start with + and the country code, for example +97339990001"` |
