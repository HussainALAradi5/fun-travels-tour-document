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


def roles(annotation):
    found = re.findall(r"'([A-Z_]+)'", annotation or "")
    return ", ".join(found) if found else ""


# ---------------------------------------------------------------- service docs used by controllers
service_docs = {}  # (ServiceClass, function) -> first sentence of its javadoc
for _d, _n, _t in java_files("services"):
    for _m in re.finditer(r"\n(?:    @[^\n]*\n)*    public [\w<>\[\], ?.]+ (\w+)\(", _t):
        _doc = javadoc_before(_t, _m.start() + 1)
        if _doc:
            service_docs.setdefault((_n, _m.group(1)), _doc.split(". ")[0].rstrip(".") + ".")


def humanize(name):
    words = " ".join(re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])", name)).lower()
    return words[:1].upper() + words[1:] + "."


URL_ROLES = {"/api/tickets": "CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER",
             "/api/reservations": "CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER",
             "/api/notifications": "CUSTOMER, ADMIN, MANAGER, EMPLOYEE, OWNER"}

# ---------------------------------------------------------------- controllers
public_get = ["/api/auth/**", "/api/tours/**", "/api/meals/**", "/api/countries/**", "/api/ports/**",
              "/api/cities/**", "/api/wallet/config"]
index_rows = []
for domain, name, text in java_files("controllers"):
    fields = dict((var, cls) for cls, var in re.findall(r"private final (\w+) (\w+);", text))
    base = re.search(r'@RequestMapping\("([^"]+)"\)', text)
    base = base.group(1) if base else ""
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
            role = "public" if http == "GET" and any(path.startswith(p.rstrip("/**")) for p in public_get) or path.startswith("/api/auth") else "any signed-in user"
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
        rows.append(f"| `{http} {path}` | {service_calls} | {purpose} | {role} | {'; '.join(request) or '-'} | `{resp}` |")
    if not rows:
        continue
    doc = [f"# {name}", "", f"Base path `{base}`. Source: `controllers/{domain}/{name}.java`.", "",
           "Errors use the shared envelope (see [errors](../../globals/errors.md)): 400 validation or bad input, "
           "401 missing/invalid token, 403 role or ownership, 404 missing record, 409 workflow or duplicate conflict.", "",
           "| Method and path | Service function | Why it is used | Role | Request | Response |",
           "| --- | --- | --- | --- | --- | --- |", *rows]
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
        methods.append((fn, f"{static or ''}{ret} {fn}({params})", doc, notes))
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
    for fn, signature, doc, notes in methods:
        lines += [f"### `{signature}`", ""]
        if doc:
            lines += [f"**Purpose:** {doc}", ""]
        if notes:
            lines += [f"**Runs in:** {'; '.join(notes)}", ""]
    write(f"services/{domain}/{name}.md", "\n".join(lines))
    service_rows.append(f"| {domain} | [{name}]({domain}/{name}.md) | {len(methods)} | {'yes' if logic else '-'} |")
write("services/README.md", "\n".join([
    "# Services", "", "Every public function with its signature, generated from the source. Services marked "
    "*business logic* also carry hand-written rules, cases, and exceptions.", "",
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
    const_lines += [f"## {name}", "", "| Name | Value |", "| --- | --- |"]
    for m in re.finditer(r"public static final [\w<>]+ (\w+) = (.+?);", text, re.S):
        const_lines.append(f"| `{m.group(1)}` | `{' '.join(m.group(2).split())}` |")
    const_lines.append("")
write("constants/README.md", "\n".join(const_lines))
print("docs generated")
