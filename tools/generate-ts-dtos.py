"""Generates TypeScript DTO mirrors of the server's Java DTOs.
Usage: python -I gen_ts_dtos.py <server-dto-dir> <client-src> <web|mobile>
One file per type: src/dtos/<domain>/<Name>Dto.ts exporting `interface <Name>Dto`."""
import os
import re
import sys

DTO_DIR, SRC, FLAVOR = sys.argv[1], sys.argv[2], sys.argv[3]
DOMAIN = {"tourmanagement": "tour-management"}

ENUMS = {
    "web": {
        "GenericStatus": "@/enums/GenericStatus", "PortType": "@/enums/PortType",
        "NotificationType": "@/enums/notification/NotificationType",
        "ReferenceType": "@/enums/notification/ReferenceType", "PaymentMethod": "@/enums/payment/PaymentMethod",
        "PaymentStatus": "@/enums/payment/PaymentStatus", "TransactionType": "@/enums/TransactionType",
        "UserRequestStatus": "@/enums/user-request/UserRequestStatus",
        "UserRequestType": "@/enums/user-request/UserRequestType",
        "ChairType": "@/enums/tour-management/ChairType", "MealDietaryType": "@/enums/tour-management/MealDietaryType",
        "SeatStatus": "@/enums/tour-management/SeatStatus", "SpiceLevel": "@/enums/tour-management/SpiceLevel",
        "TicketStatus": "@/enums/tour-management/TicketStatus",
        "TransportationStatus": "@/enums/tour-management/TransportationStatus",
        "TransportationType": "@/enums/tour-management/TransportationType", "UserTypeEnum": ("@/enums/UserType", "UserType"),
        "ReportType": "@/enums/report/ReportType", "ReportFormat": "@/enums/report/ReportFormat",
        "MediaCategory": "@/enums/media/MediaCategory",
    },
    "mobile": {
        "GenericStatus": "@/enums/GenericStatus", "PaymentMethod": "@/enums/PaymentMethod",
        "SeatStatus": "@/enums/SeatStatus", "TicketStatus": "@/enums/TicketStatus",
        "ReportType": "@/enums/ReportType", "ReportFormat": "@/enums/ReportFormat", "MediaCategory": "@/enums/MediaCategory",
        "UserRequestType": "@/enums/UserRequestType", "UserRequestStatus": "@/enums/UserRequestStatus",
        "ReferenceType": "@/enums/ReferenceType", "PaymentStatus": "@/enums/PaymentStatus",
        "TransactionType": "@/enums/TransactionType",
    },
}[FLAVOR]
# The mobile app only calls customer endpoints; it mirrors just those contracts.
MOBILE_TYPES = {
    "LoginRequest", "RegisterRequest", "AuthResponse", "UserResponse", "ProfileResponse", "UserUpdateRequest",
    "AgencySummary", "BranchSummary", "AccountResponse", "AccountSummary", "TransactionResponse", "PageResponse",
    "EntityReference", "TourResponse", "TourSummary", "CountrySummary", "CitySummary", "TransportationSummary",
    "UserSummary", "MealPlanResponse", "SeatResponse", "SeatSummary", "ReservationCreateRequest",
    "TicketSelectionRequest", "ReservationResponse", "TicketResponse", "NotificationResponse", "NotificationCounts",
    "PasswordResetRequest", "PasswordResetConfirmRequest", "CountryResponse", "PaymentResponse", "ReservationSummary",
    "UserRequestCreateRequest", "UserRequestResponse", "CommentRequest", "CommentResponse", "EventLogResponse",
    "TimelineResponse", "ReportRequest", "MediaResponse",
}
NUM = {"Integer", "int", "Double", "double", "Long", "long", "BigDecimal", "Float", "float", "Short"}

# ---- parse every DTO ----
types = {}  # name -> (domain, kind, [(field, javaType, required)], doc, generics)
for dirpath, _, files in os.walk(DTO_DIR):
    for f in files:
        if not f.endswith(".java"):
            continue
        pkg = os.path.basename(dirpath)
        text = open(os.path.join(dirpath, f), encoding="utf-8").read()
        javadoc = re.search(r"/\*\*(.*?)\*/\s*(?:@[^\n]*\n\s*)*public (?:record|class|abstract class)", text, re.S)
        doc_text = ""
        if javadoc:
            doc_lines = [line.strip().lstrip("*").strip() for line in javadoc.group(1).split("\n")]
            doc_text = " ".join(line for line in doc_lines if line and not line.startswith("@"))
            doc_text = re.sub(r"\{@code ([^}]*)\}", r"\1", doc_text)
        m = re.search(r"public record (\w+)(<\w+>)?\((.*?)\)\s*(?:implements [^{]*)?\{", text, re.S)
        if m:
            name, generic, body = m.group(1), m.group(2), m.group(3)
            body = re.sub(r"/\*.*?\*/", "", body, flags=re.S)
            parts, depth, cur = [], 0, ""
            for ch in body:
                if ch in "(<":
                    depth += 1
                elif ch in ")>":
                    depth -= 1
                if ch == "," and depth == 0:
                    parts.append(cur)
                    cur = ""
                else:
                    cur += ch
            parts.append(cur)
            fields = []
            for p in parts:
                p = " ".join(p.split())
                if not p:
                    continue
                required = bool(re.search(r"@(NotNull|NotBlank|NotEmpty)\b", p))
                p = re.sub(r"@\w+(\((?:[^()]|\([^()]*\))*\))?\s*", "", p).strip()
                jt, fn = p.rsplit(" ", 1)
                fields.append((fn, jt.strip(), required))
            types[name] = (pkg, "record", fields, doc_text, generic)
            continue
        m = re.search(r"public (?:abstract )?class (\w+)(?: extends (\w+))?", text)
        if m and ("Filter" in m.group(1)):
            name, parent = m.group(1), m.group(2)
            fields = [(fn, jt.strip(), False) for jt, fn in re.findall(r"private ([\w.<>, ]+?) (\w+)\s*[;=]", text)]
            types[name] = (pkg, "filter", fields, parent, None)


def ts_type(jt, deps):
    jt = jt.replace("java.util.", "").replace("java.time.", "").strip()
    g = re.match(r"(List|Set|Collection)<(.+)>$", jt)
    if g:
        inner = ts_type(g.group(2), deps)
        return f"{inner}[]" if re.match(r"^[\w.]+$", inner) else f"({inner})[]"
    g = re.match(r"Map<\s*String\s*,\s*(.+)>$", jt)
    if g:
        return f"Record<string, {ts_type(g.group(1), deps)}>"
    if jt in NUM:
        return "number"
    if jt in ("String", "LocalDate", "LocalDateTime", "Instant"):
        return "string"
    if jt in ("boolean", "Boolean"):
        return "boolean"
    if jt == "T":
        return "T"
    if jt in ENUMS:
        e = ENUMS[jt]
        path, alias = (e if isinstance(e, tuple) else (e, jt))
        deps[alias] = path
        return alias
    if jt in types:
        if FLAVOR == "mobile" and jt not in MOBILE_TYPES:
            return "unknown"
        deps[jt + "Dto"] = f"@/dtos/{DOMAIN.get(types[jt][0], types[jt][0])}/{jt}Dto"
        return jt + "Dto"
    return "string"  # enums the client does not model are plain strings


written = 0
for name, (pkg, kind, fields, extra, generic) in sorted(types.items()):
    if FLAVOR == "mobile" and name not in MOBILE_TYPES:
        continue
    domain = DOMAIN.get(pkg, pkg)
    deps = {}
    lines = []
    if kind == "filter":
        parent = extra
        all_fields = list(fields)
        if parent and parent in types:
            all_fields = types[parent][2] + all_fields
        if name == "GenericFilterRequest":
            continue
        doc = "Query parameters for a server-side filtered, paged list."
    else:
        all_fields = fields
        doc = extra
    is_response = kind == "record" and not name.endswith("Request") and name != "EntityReference"
    for fn, jt, required in all_fields:
        t = ts_type(jt, deps)
        if kind == "filter" or (not is_response and not required):
            lines.append(f"  {fn}?: {t};")
        elif is_response and (t.endswith("Dto") or t.endswith("Dto[]") and False):
            lines.append(f"  {fn}: {t} | null;")
        else:
            lines.append(f"  {fn}: {t};")
    imports = [f'import type {{ {alias} }} from "{path}";' for alias, path in sorted(deps.items())
               if alias != name + "Dto"]
    header = "/**\n * " + (doc + "\n * " if doc else "") + "Mirrors the server's " + name + \
        "; generated by fun-travels-tour-document/tools/generate-ts-dtos.py, do not edit by hand.\n */"
    gen = "<T>" if generic else ""
    body = "\n".join(imports) + ("\n\n" if imports else "") + header + "\n" + \
        f"export type {name}Dto{gen} = {{\n" + "\n".join(lines) + "\n};\n"
    out = os.path.join(SRC, "dtos", domain, name + "Dto.ts")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8", newline="\n").write(body)
    written += 1
print(f"{FLAVOR}: {written} DTO files")
