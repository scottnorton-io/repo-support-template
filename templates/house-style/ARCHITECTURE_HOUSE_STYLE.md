# ARCHITECTURE.md (House Style)

Think of this file as the “tour guide” for the project. If someone new walks in and asks,  
“What does this thing do, and where do I look first?” — this is where we send them.

---

## 1. What This Project Is About

**Project Name:** _[Insert Project Name]_  

**In one or two sentences:**  
Tell the story like you’re explaining it to a teammate over coffee.  
- What problem are we solving?
- Who cares about this?
- Why does it matter?

Example:  
“This service takes messy event data from several systems, normalizes it, and exposes a clean, report-friendly API for compliance and analytics.”

---

## 2. How the Project Is Laid Out

Show the folder structure, then translate it into human terms.

```text
.
├── src/
│   ├── api/
│   ├── core/
│   ├── models/
│   └── utils/
├── tests/
├── docs/
└── scripts/
```

Then describe each top-level directory in plain language. For example:

- `src/api/` — “The front door.” HTTP routes, controllers, or handlers live here.
- `src/core/` — The brains. Domain logic, rules, and decisions.
- `src/models/` — Structured data: entities, schemas, and sometimes validation.
- `src/utils/` — Small helpers used in multiple places.
- `tests/` — Guardrails and confidence boosters.
- `docs/` — Human-facing explanations: designs, notes, decisions.
- `scripts/` — One-off or repeatable ops tasks (migrations, imports, etc.).

---

## 3. The Big Pieces and What They Own

Break down the key building blocks. Keep it short, but meaningful.

### API / Interface Layer

- Handles incoming requests (HTTP, CLI, events, etc.).
- Validates input.
- Translates outside language (“a request”) into inside language (clean parameters or commands).

### Core / Domain Layer

- Contains the “rules of the game.”
- Knows what “correct behavior” looks like.
- Should not care whether it’s behind an API, a CLI, or something else.

### Data / Integration Layer

- Talks to databases, message queues, external APIs, or storage.
- Isolates the rest of the system from “how we store or fetch this.”
- Returns usable, domain-friendly objects instead of raw rows when possible.

---

## 4. How Data Flows Through

Tell the story step by step. Example:

1. A request hits the API with some input.
2. The API validates and normalizes the input.
3. The API calls a core service with a clear, typed set of parameters.
4. The core service:
   - Applies business rules.
   - Calls the data layer if it needs to read or store something.
5. The result gets wrapped into a response shape and returned to the caller.

If there are background jobs, event-driven flows, or scheduled tasks, describe them in the same kind of narrative way.

---

## 5. Configuration and Environments

Explain how this thing is wired up without leaking secrets.

- Where config lives (env vars, config files, etc.).
- What needs to be set for local development.
- Any differences between dev, test, and prod.

Keep a simple mental model:  
“If I need to run this on a new laptop or a new environment, what are the 3–5 knobs I must know about?”

---

## 6. Logging, Errors, and Observability

- What gets logged and why.
- Any IDs or correlation fields that help tie logs together.
- How errors are surfaced:
  - What gets caught and translated into a friendly message?
  - What bubbles up to cause alerts?

Make it easy for someone investigating an incident or weird behavior to know where to look first.

---

## 7. Security & Compliance Awareness

If this project touches anything sensitive (user data, Account Data (AD), PCI-ish workflows, secrets, etc.), spell out the important boundaries:

- Which components handle sensitive data.
- What we **never** log.
- Any encryption or tokenization steps.
- Pointers to `SECURITY_STANDARDS.md` or other security docs.

The goal is not to restate the entire standard. The goal is to help someone avoid shooting themselves in the foot.

---

## 8. How to Extend or Change Things Safely

Help future-you and future-teammates answer:

- “Where should I plug in a new feature?”
- “What are the patterns I should copy, not reinvent?”
- “What should I absolutely not break?”

Example sections:

- Adding a new API endpoint
- Adding a new background job
- Adding a new data source

Keep each as a short, step-by-step story.

---

## 9. Known Gaps / Future Improvements

Be honest and kind to the next person:

- What’s currently a bit messy?
- What would you refactor if you had a week?
- What tech debt is “intentional” versus “oops”?

This is where you give people permission to improve things, not just duct tape more on.

---

## 10. Quick Glossary

List any terms, abbreviations, or internal language that might confuse someone new.  

Example:

- **ADE** — Account Data Environment; similar to CDE, but scoped to all Account Data (AD).
- **AD** — Account Data (CHD + SAD); the stuff we must protect.
