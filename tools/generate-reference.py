"""Generate layer-mirrored reference docs from the server source.

Usage: python -I gen_docs.py <server_root> <docs_root>
Writes docs_root/server/{controllers,services,models,enums,constants}. Hand-written business
logic for services is read from docs_root/tools/service-logic/<Service>.md when present.
"""
import os
import re
import sys

SRC = os.path.join(sys.argv[1], "src", "main", "java", "com", "server", "server")
OUT = os.path.join(sys.argv[2], "server")
LOGIC = os.path.join(sys.argv[2], "tools", "service-logic")


def read(path):
    return open(path, encoding="utf-8").read()


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8", newline="\n").write(text.rstrip() + "\n")


def java_files(layer):
    base = os.path.join(SRC, layer)
    for d, _, fs in os.walk(base):
        for f in sorted(fs):
            if f.endswith(".java"):
                yield os.path.relpath(d, base).replace(os.sep, "/"), f[:-5], read(os.path.join(d, f))


def javadoc_before(text, index):
    """The javadoc directly above a declaration (only annotations may sit in between)."""
    head = text[:index]
    start = head.rfind("/**")
    end = head.rfind("*/")
    if start < 0 or end < start or not re.fullmatch(r"\s*(?:@[^\n]*\n\s*)*", head[end + 2:]):
        return ""
    doc = re.sub(r"\s*\*\s?", " ", head[start + 3:end]).strip()
    doc = re.sub(r"\{@(?:link|code) ([^}]*)\}", r"`\1`", doc)
    return doc.split(" @")[0].strip()


# Exception -> HTTP status, as mapped in middlewares/errors/GlobalExceptionHandler.
STATUS = {"ResourceNotFoundException": 404, "DuplicateResourceException": 409, "AccessDeniedException": 403,
          "WorkflowException": 409, "IllegalArgumentException": 400, "IllegalStateException": 409,
          "StorageException": 500, "ExternalServiceException": 502, "BadCredentialsException": 401,
          "DisabledException": 403, "UsernameNotFoundException": 401}


def api_prefix():
    props = read(os.path.join(SRC, "config", "properties", "AppProperties.java"))
    found = re.search(r'@DefaultValue\("([^"]+)"\)\s*@NotBlank String apiPrefix', props)
    return found.group(1) if found else "/api"


API = api_prefix()


def method_bodies(text):
    """name -> body of every method declared at class level (4-space indent), found by counting braces."""
    bodies = {}
    for m in re.finditer(r"\n    (?:public|protected|private)[^\n;=]*? (\w+)\([^;{]*\)[^;{]*\{", text):
        depth, i = 1, m.end()
        while depth and i < len(text):
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        bodies[m.group(1)] = bodies.get(m.group(1), "") + text[m.end():i]
    return bodies


def thrown(body):
    """(exception, workflow code or None, message) for each throw in a method body."""
    found = []
    for m in re.finditer(r"new (\w+Exception)\(", body):
        exc = m.group(1)
        if exc not in STATUS:
            continue
        depth, i = 1, m.end()
        while depth and i < len(body):
            depth += {"(": 1, ")": -1}.get(body[i], 0)
            i += 1
        args = body[m.end():i - 1]
        strings = re.findall(r'"((?:[^"\\]|\\.)*)"', args)
        code = strings[0] if exc == "WorkflowException" and len(strings) > 1 and re.fullmatch(r"[A-Z_]+", strings[0]) else None
        message = " ".join(s for s in strings if s != code).strip()
        if exc == "ResourceNotFoundException" and len(strings) == 1 and not re.search(r"\bfound\b", message):
            message += " not found"
        found.append((exc, code, message))
    if "DomainWorkflowValidator.validate" in body:
        found.append(("WorkflowException", None, "Status change not allowed by the workflow"))
    if re.search(r"accessPolicy\.require\w*\(|requireAgency\w*\(|requireMember\(", body):
        found.append(("AccessDeniedException", None, "Caller lacks the role, ownership, or agency access"))
    return found


def exceptions_by_method(text):
    """Throws per method, including those of the private helpers it calls in the same class."""
    bodies = method_bodies(text)
    direct = {name: thrown(body) for name, body in bodies.items()}
    calls = {name: {other for other in bodies if other != name and re.search(r"(?<![.\w])" + other + r"\(", body)}
             for name, body in bodies.items()}
    result = {}
    for name in bodies:
        seen, stack, out = set(), [name], []
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            out += direct.get(current, [])
            stack += sorted(calls.get(current, ()))
        result[name] = list(dict.fromkeys(out))
    return result


def roles(annotation):
    found = re.findall(r"'([A-Z_]+)'", annotation or "")
    return ", ".join(found) if found else ""


# ---------------------------------------------------------------- service docs used by controllers
service_docs = {}  # (ServiceClass, function) -> first sentence of its javadoc
service_exceptions = {}  # (ServiceClass, function) -> [(exception, code, message)]
for _d, _n, _t in java_files("services"):
    for _fn, _found in exceptions_by_method(_t).items():
        service_exceptions[(_n, _fn)] = _found
    for _m in re.finditer(r"\n(?:    @[^\n]*\n)*    public [\w<>\[\], ?.]+ (\w+)\(", _t):
        _doc = javadoc_before(_t, _m.start() + 1)
        if _doc:
            service_docs.setdefault((_n, _m.group(1)), _doc.split(". ")[0].rstrip(".") + ".")


def humanize(name):
    words = " ".join(re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])", name)).lower()
    return words[:1].upper() + words[1:] + "."


URL_ROLES = {API + "/tickets": "CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER",
             API + "/reservations": "CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER",
             API + "/notifications": "CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER"}

# ---------------------------------------------------------------- controllers
public_get = [API + p for p in ("/auth/**", "/tours/**", "/meals/**", "/countries/**", "/ports/**", "/cities/**",
                                "/wallet/config")]
index_rows = []
for domain, name, text in java_files("controllers"):
    fields = dict((var, cls) for cls, var in re.findall(r"private final (\w+) (\w+);", text))
    base = re.search(r'@RequestMapping\("([^"]+)"\)', text)
    base = API + (base.group(1) if base else "")
    rows = []
    for m in re.finditer(r'((?:\s*@(?:PreAuthorize|GetMapping|PostMapping|PutMapping|PatchMapping|DeleteMapping)[^\n]*\n)+)\s*public\s+ResponseEntity<(.+?)>\s+(\w+)\((.*?)\)\s*(?:throws [\w, ]+)?\{(.*?)\n    \}', text, re.S):
        annotations, response, method_name, params, body = m.groups()
        verb = re.search(r"@(Get|Post|Put|Patch|Delete)Mapping(?:\((?:value = )?\"?([^\",)]*)\"?)?", annotations)
        http = verb.group(1).upper()
        path = (base + (verb.group(2) or "")).replace(":\\\\d+", "").replace(":\\d+", "")
        pre = re.search(r"@PreAuthorize\((.*)\)", annotations)
        role = roles(pre.group(1)) if pre else ""
        if not role:
            role = next((v + " (URL rule)" for k, v in URL_ROLES.items() if path.startswith(k)), "")
        if not role:
            role = "public" if http == "GET" and any(path.startswith(p.rstrip("/**")) for p in public_get) or path.startswith(API + "/auth") else "any signed-in user"
        services = sorted(set(re.findall(r"(\w+(?:Service|service))\.(\w+)\(", body)))
        service_calls = ", ".join(f"`{fields.get(s, s)}.{fn}`" for s, fn in services if s != "modelMapper") or "-"
        body_dto = re.search(r"@RequestBody\s+(\w+(?:<[^>]+>)?)\s+\w+", params)
        query = re.findall(r"@(?:RequestParam|ModelAttribute)[^,]*?\s(\w+(?:<\w+>)?)\s+(\w+)(?:,|$)", params)
        request = []
        if body_dto:
            request.append(f"body `{body_dto.group(1)}`")
        if query:
            request.append("query " + ", ".join(f"`{n}`" for _, n in query))
        resp = re.sub(r"^ApiResponse<(.*)>$", r"\1", response.strip())
        called = [(fields.get(s, s), fn) for s, fn in services if s != "modelMapper"]
        purpose = javadoc_before(text, m.start()) or next(
            (service_docs[key] for key in called if key in service_docs), humanize(method_name))
        raised = [found for key in called for found in service_exceptions.get(key, [])]
        statuses = {STATUS[exc] for exc, _, _ in raised}
        if "@Valid" in params or request:
            statuses.add(400)
        if role != "public":
            statuses.add(401)
        if pre or "(URL rule)" in role:
            statuses.add(403)
        codes = sorted({code for _, code, _ in raised if code})
        errors = ", ".join(str(s) for s in sorted(statuses)) or "-"
        if codes:
            errors += " (" + ", ".join(f"`{c}`" for c in codes) + ")"
        rows.append(f"| `{http} {path}` | {service_calls} | {purpose} | {role} | {'; '.join(request) or '-'} | `{resp}` | {errors} |")
    if not rows:
        continue
    doc = [f"# {name}", "", f"Base path `{base}`. Source: `controllers/{domain}/{name}.java`.", "",
           "Errors use the shared envelope and codes in [errors](../../globals/errors.md). The Exceptions column lists "
           "the statuses an endpoint can return (workflow codes in brackets), derived from the service functions it "
           "calls; each service page lists the cases behind them.", "",
           "| Method and path | Service function | Why it is used | Role | Request | Response | Exceptions |",
           "| --- | --- | --- | --- | --- | --- | --- |", *rows]
    write(f"controllers/{domain}/{name}.md", "\n".join(doc))
    index_rows.append(f"| {domain} | [{name}]({domain}/{name}.md) | `{base}` | {len(rows)} |")
write("controllers/README.md", "\n".join([
    "# Controllers", "", "Generated from the controller source; one file per controller, grouped by domain.", "",
    "| Domain | Controller | Base path | Endpoints |", "| --- | --- | --- | --- |", *index_rows]))

# ---------------------------------------------------------------- services
service_rows = []
for domain, name, text in java_files("services"):
    if "abstract class" in text and domain == "common" and name == "GenericFilterService":
        pass
    methods = []
    throws_of = exceptions_by_method(text)
    for m in re.finditer(r"\n((?:    @[^\n]*\n)*)    (public|protected) (static )?([\w<>\[\], ?.]+) (\w+)\(([^)]*)\)", text):
        annotations, visibility, static, ret, fn, params = m.groups()
        if fn == name:
            continue
        params = re.sub(r"@\w+(\([^)]*\))?\s+", "", " ".join(params.split()))
        tx = "read-only transaction" if "readOnly = true" in annotations else ("transaction" if "@Transactional" in annotations else "")
        pre = re.search(r"@PreAuthorize\((.*)\)", annotations)
        sched = re.search(r"@Scheduled\(([^)]*)\)", annotations)
        notes = [n for n in [tx, f"roles: {roles(pre.group(1))}" if pre else "", f"scheduled `{sched.group(1)}`" if sched else ""] if n]
        doc = javadoc_before(text, m.start() + 1)
        methods.append((fn, f"{static or ''}{ret} {fn}({params})", doc, notes, throws_of.get(fn, [])))
    if not methods:
        continue
    class_doc = javadoc_before(text, text.find("public class") if "public class" in text else text.find("class "))
    logic_path = os.path.join(LOGIC, name + ".md")
    logic = read(logic_path) if os.path.exists(logic_path) else ""
    lines = [f"# {name}", "", f"Source: `services/{domain}/{name}.java`.", ""]
    if class_doc:
        lines += [class_doc, ""]
    if logic:
        lines += [logic.strip(), ""]
    lines += ["## Functions", ""]
    for fn, signature, doc, notes, raised in methods:
        lines += [f"### `{signature}`", ""]
        if doc:
            lines += [f"**Purpose:** {doc}", ""]
        if notes:
            lines += [f"**Runs in:** {'; '.join(notes)}", ""]
        if raised:
            lines += ["**Cases and exceptions:**", "", "| Case | Exception | Status |", "| --- | --- | --- |"]
            for exc, code, message in raised:
                lines.append(f"| {message or '-'} | `{exc}`{' `' + code + '`' if code else ''} | {STATUS[exc]} |")
            lines.append("")
        else:
            lines += ["**Exceptions:** none of its own; failures come from the functions it calls.", ""]
    write(f"services/{domain}/{name}.md", "\n".join(lines))
    service_rows.append(f"| {domain} | [{name}]({domain}/{name}.md) | {len(methods)} | {'yes' if logic else '-'} |")
write("services/README.md", "\n".join([
    "# Services", "", "Every public function in source order: signature, purpose, transaction and role notes, and the "
    "cases it rejects with their exception and status (its own throws and those of the private helpers it calls). "
    "Services marked *business logic* also carry hand-written rules.", "",
    "| Domain | Service | Functions | Business logic |", "| --- | --- | --- | --- |", *service_rows]))

# ---------------------------------------------------------------- models
model_rows, relation_rows = [], []
for domain, name, text in java_files("models"):
    if "@Entity" not in text and "@MappedSuperclass" not in text:
        continue
    table = re.search(r'@Table\(name = "([^"]+)"', text)
    parent = re.search(r"class \w+ extends (\w+)", text)
    fields = []
    for m in re.finditer(r"((?:\s*@[^\n]*\n)*)\s*private ([\w<>, .]+) (\w+)( = [^;]+)?;", text):
        ann, ftype, fname, default = m.groups()
        rel = re.search(r"@(ManyToOne|OneToMany|OneToOne|ManyToMany)", ann)
        col = re.search(r'@JoinColumn\(name = "([^"]+)"', ann)
        flags = []
        if "unique = true" in ann:
            flags.append("unique")
        if "nullable = false" in ann or "@NotNull" in ann or "@NotBlank" in ann:
            flags.append("required")
        if "@Transient" in ann:
            flags.append("not stored")
        if rel:
            cascade = re.search(r"cascade = ([\w.]+)", ann)
            mapped = re.search(r'mappedBy = "(\w+)"', ann)
            target = re.sub(r".*<(\w+)>", r"\1", ftype)
            relation_rows.append(f"| {name} | {rel.group(1)} | {target} | `{fname}` | "
                                 f"{('`' + col.group(1) + '`') if col else ('mapped by `' + mapped.group(1) + '`' if mapped else '-')} | "
                                 f"{cascade.group(1).replace('CascadeType.', '') if cascade else '-'} |")
        fields.append(f"| `{fname}` | `{ftype}` | {rel.group(1) if rel else ''} {', '.join(flags)} |")
    lines = [f"# {name}", "", f"Table `{table.group(1) if table else '-'}`. Inherits `{parent.group(1) if parent else '-'}`. "
             f"Source: `models/{domain}/{name}.java`.", "", "| Field | Type | Notes |", "| --- | --- | --- |", *fields]
    write(f"models/{domain}/{name}.md", "\n".join(lines))
    model_rows.append(f"| {domain} | [{name}]({domain}/{name}.md) | `{table.group(1) if table else '(mapped superclass)'}` | {parent.group(1) if parent else '-'} |")
write("models/README.md", "\n".join([
    "# Models", "", "Every persisted model extends [BaseEntity](base/BaseEntity.md): `id`, unique `code`, "
    "`createdAt`, `updatedAt`, `createdBy`, `updatedBy`. Equality is by type and id.", "",
    "| Domain | Model | Table | Inherits |", "| --- | --- | --- | --- |", *model_rows, "",
    "## Relationships", "", "| Model | Relation | Target | Field | Foreign key | Cascade |",
    "| --- | --- | --- | --- | --- | --- |", *relation_rows]))

# ---------------------------------------------------------------- enums & constants
enum_lines = ["# Enums", "", "| Domain | Enum | Values |", "| --- | --- | --- |"]
for domain, name, text in java_files("enums"):
    body = re.search(r"enum \w+ \{(.*?)\}", text, re.S).group(1)
    body = re.sub(r"//[^\n]*", "", body).split(";")[0]
    values = [v.strip() for v in body.split(",") if v.strip()]
    enum_lines.append(f"| {domain} | `{name}` | {', '.join('`' + v + '`' for v in values)} |")
write("enums/README.md", "\n".join(enum_lines))

const_lines = ["# Constants", "", "Shared values live in `constants/`; services never repeat them inline.", ""]
for domain, name, text in java_files("constants"):
    const_lines += [f"## {domain}/{name}", "", "| Name | Value |", "| --- | --- |"]
    for m in re.finditer(r"public static final [\w<>]+ (\w+) = (.+?);", text, re.S):
        const_lines.append(f"| `{m.group(1)}` | `{' '.join(m.group(2).split())}` |")
    const_lines.append("")
write("constants/README.md", "\n".join(const_lines))


# ---------------------------------------------------------------- DTOs
def split_components(header):
    """Record components at nesting depth zero."""
    parts, depth, cur = [], 0, ""
    for ch in re.sub(r"/\*.*?\*/", "", header, flags=re.S):
        depth += ch in "(<"
        depth -= ch in ")>"
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    return [" ".join(p.split()) for p in parts + [cur] if p.strip()]


def rules(annotations):
    found = []
    for name, arg in re.findall(r"@(\w+)(\((?:[^()]|\([^()]*\))*\))?", annotations):
        if name in ("Valid",):
            found.append("nested values validated")
        elif name in ("NotNull", "NotBlank", "NotEmpty"):
            found.append("required" if name == "NotNull" else "required, not blank")
        elif name in ("Pattern", "Size", "Min", "Max", "Positive", "PositiveOrZero", "Email", "DecimalMin", "DecimalMax"):
            msg = re.search(r'message = "([^"]+)"', arg or "")
            if "MOBILE_NUMBER" in (arg or ""):
                found.append("+ country code and number, e.g. +97339990001 (E.164)")
                continue
            value = re.search(r"(?:value|max|min) = ([^,)]+)", arg or "")
            found.append(msg.group(1) if msg else f"{name}{'(' + value.group(1) + ')' if value else ''}")
    return "; ".join(dict.fromkeys(found))


dto_index, dto_pages = [], {}
for domain, name, text in java_files("dto"):
    record = re.search(r"public record (\w+)(<\w+>)?\((.*?)\)\s*(?:implements [^{]*)?\{", text, re.S)
    doc = javadoc_before(text, record.start() if record else text.find("public "))
    doc = re.sub(r"@param\s.*$", "", doc).strip()
    rows = []
    if record:
        kind = "request record" if name.endswith("Request") or name == "EntityReference" else "response record"
        for part in split_components(record.group(3)):
            annotations = " ".join(re.findall(r"@\w+(?:\((?:[^()]|\([^()]*\))*\))?", part))
            plain = re.sub(r"@\w+(\((?:[^()]|\([^()]*\))*\))?\s*", "", part).strip()
            ftype, fname = plain.rsplit(" ", 1)
            rows.append(f"| `{fname}` | `{ftype}` | {rules(annotations) or '-'} |")
        factories = re.findall(r"public static \w+(?:<\w+>)? (\w+)\((\w+)", text)
        built = ", ".join(f"`{f}({p})`" for f, p in factories if f != "empty")
    else:
        kind = "query parameters (class)"
        parent = re.search(r"extends (\w+)", text)
        for m in re.finditer(r"private ([\w<>, .]+) (\w+);", text):
            rows.append(f"| `{m.group(2)}` | `{m.group(1)}` | optional |")
        if parent:
            rows.insert(0, f"| (inherited) | `{parent.group(1)}` | `page`, `size`, `search`, `sortBy`, `sortDir` |")
        built = "bound from the query string"
    page = dto_pages.setdefault(domain, [f"# {domain} DTOs", "",
                                          f"Source: `dto/{domain}/`. Clients mirror these in `src/dtos/{domain.replace('tourmanagement', 'tour-management')}/`.", ""])
    page += [f"## {name}", "", f"{kind}{'; built by ' + built if built else ''}.{(' ' + doc) if doc else ''}", "",
             "| Field | Type | Rules |", "| --- | --- | --- |", *rows, ""]
    dto_index.append(f"| {domain} | [{name}]({domain}/README.md#{name.lower()}) | {kind} |")
for domain, page in dto_pages.items():
    write(f"dto/{domain}/README.md", "\n".join(page))
write("dto/README.md", "\n".join([
    "# DTOs", "",
    "Every request and response body is a Java record in `dto/<domain>/`, one type per file. Entities never cross the "
    "API boundary.", "",
    "- Requests carry Bean Validation annotations; a compact constructor may normalize input before validation "
    "(mobile numbers drop spaces and a leading 00).",
    "- Responses are built by a static `from(entity)` factory next to their shape; there is no mapper class. "
    "Nested references use shared summary records (`UserSummary`, `CountrySummary`, `TourSummary`, ...).",
    "- Filter DTOs stay classes because they inherit the shared paging fields of `GenericFilterRequest` and are "
    "bound from the query string.",
    "- The web client and the mobile app mirror these as `src/dtos/<domain>/<Name>Dto.ts`, generated by "
    "`tools/generate-ts-dtos.py`; rerun it after changing a DTO.", "",
    "| Domain | DTO | Kind |", "| --- | --- | --- |", *dto_index]))
print("docs generated")
