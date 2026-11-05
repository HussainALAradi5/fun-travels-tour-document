# Documentation Standard

1. **Layer-mirrored layout.** `server/` keeps `models`, `services`, `controllers`, `enums`, `constants`, and `globals`, each with domain subfolders matching the code (`services/tourmanagement/TicketService.md`). No per-feature folders. Clients and mobile have their own sections.
2. **Generated reference, hand-written rules.** Signatures, endpoint tables, model fields, and enums are generated from source so they cannot drift. Business logic, cases, and exceptions are written in `tools/service-logic/<Service>.md` and merged into the generated page.
3. **Services.** Each function in source order: signature, purpose, transaction and role notes, and a cases table of what it rejects with the exception and status (generated from its throws and its private helpers); workflow services add hand-written business logic.
4. **Controllers.** One table per controller: method and path, service function, why it is used, role, request and response DTO, and the statuses it can return; the error codes are listed once in [errors](server/globals/errors.md).
5. **Use cases** state actor, preconditions, main flow, alternate and failure flows, and resulting state.
6. **Claims match evidence.** Only flows listed in [verification](verification/README.md) are described as verified. Untested integrations (card payments, email delivery, devices) are marked as such.
7. No secrets, production credentials, or real customer data.
8. **Phases.** [phases](phases/README.md) holds one folder per phase; a phase is marked done only with the checks that prove it.
