#!/usr/bin/env python3
"""
promptgen.py

Prints and optionally copies the Repo Support File Generator Prompt
to your clipboard for easy use in an AI assistant.
"""

import textwrap

try:
    import pyperclip
    HAS_PYPERCLIP = True
except ImportError:
    HAS_PYPERCLIP = False


PROMPT = textwrap.dedent("""
[Paste the contents of REPO_SUPPORT_GENERATOR_PROMPT.md here verbatim]
""").strip()


def main() -> None:
    print("\n=== Repo Support Generator Prompt ===\n")
    print(PROMPT)

    if HAS_PYPERCLIP:
        try:
            pyperclip.copy(PROMPT)
            print("\n✅ Prompt copied to clipboard.")
        except Exception:
            print("\n⚠️ pyperclip is installed but clipboard copy failed.")
    else:
        print("\nℹ️ pyperclip not installed. To enable clipboard copy, run:")
        print("    pip install pyperclip")


if __name__ == "__main__":
    main()
