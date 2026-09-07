# User Interface

**File:** `src/interface/UserInterface.ts`

## Types

### User
```typescript
interface User {
  id?: number;
  userName: string;
  name: string;
  email: string;
  password?: string;
  age: number;
  userType: UserType;
  mobileNumber: string;
  profileImageUrl?: string;
  agency?: Agency;
  agencyBranch?: AgencyBranch;
  active: boolean;
}
```

### DEFAULT_USER
Constant with empty defaults for form initialization.

### mapUsersToExportFormat(users)
Maps user array to flat format for Excel/PDF export.
