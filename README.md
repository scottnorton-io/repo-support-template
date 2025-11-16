# Repo Support Template (with House Style)

This repository is a **universal template** for generating high-quality, AI-assisted support files for any GitHub project.

It includes:

- A reusable **Repo Support File Generator Prompt**
- General-purpose templates for:
  - `AI_ASSISTANT.md`
  - `ARCHITECTURE.md`
  - `CONTRIBUTING.md`
  - `SECURITY_STANDARDS.md`
  - Project `README.md`
- **House-style variants** tuned for:
  - PCI DSS / compliance-heavy environments
  - Narrative, friendly, and empathetic documentation
  - Practical, human-first guidance (not stiff corporate speak)
- A CLI helper to copy the prompt into your clipboard
- A GitHub Issue template to remind you to generate support files

Use this repo as your **starting point** or as a **central toolkit** for standardizing architecture, documentation, and AI collaboration across all your projects.

---

## 🔧 How to Use

### 1. As a Toolkit Repo (recommended)

1. Clone this repo locally:
   ```bash
   git clone https://github.com/<your-username>/repo-support-template-house-style.git
   ```
2. Open `generator/REPO_SUPPORT_GENERATOR_PROMPT.md`.
3. Copy the entire prompt into your AI assistant (ChatGPT or similar).
4. Provide the target repository URL or its file tree.
5. Paste the generated files into the target repository:
   - `AI_ASSISTANT.md`
   - `ARCHITECTURE.md`
   - `CONTRIBUTING.md`
   - `SECURITY_STANDARDS.md` (if relevant)
   - Updated `README.md`

Choose either the **standard templates** in `templates/` or the **house-style templates** in `templates/house-style/` depending on the tone and audience you want.

---

### 2. As a Template for New Projects

1. Mark this repo as a **template repository** in GitHub.
2. Click **Use this template** to create a new project based on it.
3. Update the files in `templates/` and/or `templates/house-style/` to match your project.
4. Use `.github/ISSUE_TEMPLATE/generate-support-files.yml` to remind yourself (or your team) to generate / refresh the support files.

---

### 3. Using the CLI Helper

The CLI script `generator/promptgen.py` prints the Repo Support File Generator Prompt and (optionally) copies it to your clipboard.

1. Install dependencies:
   ```bash
   pip install pyperclip
   ```
2. Run:
   ```bash
   python generator/promptgen.py
   ```
3. Paste the prompt into your AI assistant and follow directions.

---

## 📁 What’s Inside

- `templates/` — Standard, neutral templates for all support files.
- `templates/house-style/` — House-style templates tuned for:
  - PCI DSS / compliance programs
  - Security and GRC teams
  - Narrative, human-first documentation
- `generator/REPO_SUPPORT_GENERATOR_PROMPT.md` — The universal prompt.
- `generator/promptgen.py` — Helper to print/copy the prompt.
- `.github/ISSUE_TEMPLATE/generate-support-files.yml` — GitHub Issue template to kick off support file generation.

---

## 💡 Recommended Workflow

For each new or existing repo:

1. Open this template repo.
2. Run `promptgen.py` or copy the prompt from `REPO_SUPPORT_GENERATOR_PROMPT.md`.
3. In your AI assistant:
   - Paste the prompt
   - Provide the target repo
   - Get back fully customized support files
4. Add the generated files to the target repo.
5. Optionally customize them further by hand — using house-style templates when you want the content to feel more conversational, empathetic, and PCI-aware.

This keeps your ecosystem consistent, secure, and easy to navigate—for both humans and AI assistants.
