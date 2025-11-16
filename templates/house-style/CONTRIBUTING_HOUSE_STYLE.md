# Contributing Guide (House Style)

First things first: thanks for being here. Whether you’re fixing a tiny typo or shaping a big new feature, you’re part of the story this project is telling.

This guide is here to make contributing feel **clear, calm, and doable** — not like walking into a compliance audit with no prep.

---

## 1. How We Work Together

- Be kind.
- Be clear.
- Assume good intent.
- Ask questions early rather than silently struggle.

We’re not judging perfection; we’re building something useful together.

---

## 2. Getting Set Up

High-level steps (fill in repo-specific commands when you use this template):

1. Fork the repo and clone your fork.
2. Install dependencies.
3. Run the tests (or at least the quick ones).
4. Confirm you can run the app, script, or service.

Think of this like a small “onboarding checklist” for your local environment.

---

## 3. Branches: Keep It Simple

We aim for something like this:

- `main` — the “safe to deploy” branch.
- `feature/<short-name>` — new functionality.
- `fix/<short-name>` — bug fixes.
- `chore/<short-name>` — cleanup, tooling, or non-feature work.

Example:

```bash
git checkout -b feature/add-ade-report-summary
```

---

## 4. Commits: Tell the Story

A good commit message answers: *“What changed, and why does it matter?”*

Use a light structure like:

- `feat: add ADE summary report generator`
- `fix: handle null merchant IDs in mapper`
- `docs: clarify PCI scope narrative for req 3`
- `refactor: split data loader into smaller pieces`

Short, honest, and human-readable wins.

---

## 5. Pull Requests: Make Review Easy

When you open a PR, help your reviewer succeed:

- Keep the change focused if you can.
- Explain the context in a few sentences.
- Call out anything you’re unsure about.

Suggested PR template:

```markdown
## Summary
Briefly explain what this PR does in plain language.

## Details
- Key changes
- Any new dependencies or tools
- Any migrations or manual steps

## Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual checks (list what you tried)

## Notes
Anything reviewers should pay particular attention to.
```

---

## 6. Coding Style & House Rules

- Follow the patterns already in the repo where possible.
- Keep functions small and focused.
- Favor clarity over cleverness — especially in compliance or security-related areas.
- If you’re touching core logic or compliance narratives, add a quick comment or docstring explaining the reasoning.

---

## 7. Using AI in This Repo

AI is welcome here — as long as you’re in the driver’s seat.

- Ask the AI to follow `AI_ASSISTANT.md`.
- Treat AI output like a **draft from a smart but unfamiliar teammate**.
- Check for:
  - Security issues
  - PCI-related leaks (logging AD, mishandling data)
  - Architectural mismatches

If the AI gives you three options, pick the one that’s **simplest and safest**, not just the fanciest.

---

## 8. Security, PCI, and Sensitive Data

If you touch anything that even *smells* like Account Data (AD), PII, or regulated workflows:

- Do not log the data.
- Do not stash it in temporary files without a reason and safeguards.
- Refer to `SECURITY_STANDARDS.md` for the ground rules.
- Call out security-impacting changes explicitly in your PR description.

Think of it as “compliance as a safety net,” not “compliance as a chore.”

---

## 9. When You’re Stuck

It’s okay to say:

> “I’m not sure this is the right design, but here’s my thinking.”

You can:

- Open a draft PR.
- Open an issue with a proposal.
- Ask for help on a specific function, flow, or requirement.

We’re here to build something secure and sustainable — **together**, not solo.
