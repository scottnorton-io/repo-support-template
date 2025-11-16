# Security Standards (House Style)

This project treats security like seatbelts: you don’t notice them when things are smooth, but you’re very glad they’re there when something goes sideways.

These guidelines exist to help us protect users, Account Data (AD), and the business — without turning every change into a three-hour meeting.

---

## 1. Core Principles (Human Edition)

- **Least privilege:** Give systems and people only what they need, nothing more.
- **Defense in depth:** Don’t rely on a single control. Stack them in layers.
- **Fail safely:** When something breaks, it should not break *open*.
- **Secure by default:** The easy path should also be the safe path.

If you have to pick between slightly slower and much safer, lean toward safer — especially around AD and sensitive data.

---

## 2. Inputs, Outputs, and Messy Reality

- Treat anything that comes from outside the system as untrusted:
  - HTTP requests
  - Webhooks
  - CLI arguments
  - Files
- Validate, normalize, and reject bad or unexpected input early.
- Encode or sanitize outputs where needed (HTML, JSON, logs, etc.) to avoid injection issues.

Rule of thumb: **Never assume “they’ll send it correctly.”**

---

## 3. Authentication & Authorization (If This Project Has Them)

- Use battle-tested libraries instead of rolling your own auth.
- Centralize permission checks so we don’t scatter “who can do what” across the codebase.
- Log meaningful auth events:
  - Successful logins
  - Failed logins
  - Permission denials (without exposing sensitive details)

For anything admin-like or ADE-adjacent, be extra cautious. Add a second layer of checks or monitoring where it makes sense.

---

## 4. Secrets: Handle With Care

- No secrets in code. Ever.
- Use environment variables, secret managers, or config stores.
- If a secret leaks into a repo:
  1. Rotate it.
  2. Treat it as compromised.
  3. Clean up history if practical.

Examples of “secret” include:

- API keys
- DB passwords
- Private keys
- Tokens
- Credentials for test systems that could be escalated

---

## 5. Logging and Monitoring Without Oversharing

**Log:**
- What happened
- Where it happened
- Enough context to debug

**Do not log:**
- Full PANs or sensitive Account Data (AD)
- Passwords or secrets
- Big blobs of raw user content where it’s not necessary

When in doubt, log **pointers**, not raw sensitive content.

---

## 6. Cryptography and “Please Don’t Invent Your Own”

- Use well-known, well-reviewed crypto libraries.
- Follow recommended algorithms and key sizes.
- Don’t build your own encryption or hashing scheme because it “seems straightforward.”

If you’re unsure, flag it in a comment or PR and ask for a second set of eyes.

---

## 7. PCI DSS & Account Data (AD) Awareness

If this project touches payment flows, ADE, or anything PCI-relevant:

- Treat all Account Data (AD) as hot: handle it carefully and intentionally.
- Don’t store AD unless there’s a documented reason.
- Don’t log AD.
- Prefer tokenization, truncation, or “no AD at all” where possible.

This is less about “chasing checkboxes” and more about **keeping people out of breach headlines**.

---

## 8. Dependencies and Supply Chain

- Use maintained, reputable libraries.
- Run dependency checks regularly (`npm audit`, `pip-audit`, etc., as applicable).
- Drop unused dependencies instead of letting them linger.

Each dependency is a small trust decision; make it consciously.

---

## 9. Testing Security-Relevant Behavior

When you change something in these areas:

- Input validation
- Permissions
- Sensitive data flows
- Logging behavior

Add or update tests that prove “this works the way we think it does.”

---

## 10. If You See Something Odd…

If something feels off — a suspicious pattern, an unexpected data flow, logging too much — you don’t need to be 100% certain to speak up.

- Open a private note to maintainers.
- Add a comment and mark it as a concern.
- Propose a fix if you see one, or just raise the flag.

Security is everyone’s job, but it does **not** have to be everyone’s full-time job. These rules are here to make it easier to “do the right thing” on regular Tuesdays.
