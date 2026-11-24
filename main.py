#!/usr/bin/env python3
"""Warning Label for Humans: writes the entry line to /output/entry.txt."""
import os

LINE = (
    "WARNING: Contents under pressure. May explode over minor inconveniences, "
    "reply 'k' to heartfelt paragraphs, and cry in the shower. Handle with snacks."
)


def validate(text):
    """Gate self-check: one line, UTF-8, 1 to 160 characters, not blank."""
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")


def main():
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
