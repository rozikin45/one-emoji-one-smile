#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the hugging face.
Why this one: it reads as warm and friendly at first glance, is universal
across ages and backgrounds, feels deliberately chosen rather than the
default smiley, and works from a stranger with no intimacy or irony.
"""
from pathlib import Path

EMOJI = "\U0001F917"  # 🤗 hugging face


def main() -> None:
    # Self-check against the competition gate before writing: exactly one
    # emoji, 1-8 characters, UTF-8, not only whitespace.
    text = EMOJI
    assert 1 <= len(text) <= 8, "entry must be 1-8 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text.encode("utf-8"), "entry must be valid UTF-8"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
