#!/usr/bin/env python3
"""One Word, First Thought -- make.fun entry.

Holds the entry as a constant, checks it against the kit's gate, and
writes it to /output/entry.txt. Python 3.13, standard library only,
no network access.
"""

from pathlib import Path

ENTRY = "petrichor"

OUTPUT_PATH = Path("/output/entry.txt")


def gate_check(text: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-24 characters, not only
    whitespace, exactly one word with no surrounding whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 24:
        raise ValueError(f"entry must be 1-24 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must contain no whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must contain no control characters")
    if not text.isalpha():
        raise ValueError("entry must be a single word of letters only")
    text.encode("utf-8")


def main() -> None:
    gate_check(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)}-character entry to {OUTPUT_PATH}: {ENTRY!r}")


if __name__ == "__main__":
    main()
