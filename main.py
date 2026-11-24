#!/usr/bin/env python3
"""One Emoji, One Smile entrypoint.

Writes exactly one emoji to /output/entry.txt for the make.fun bounty
(u-0xkianno-one-emoji-one-smile-5470751f). The winning emoji is defined as a
constant and validated (1-8 chars, not only whitespace) before it is written.
"""

from pathlib import Path

# Winning entry emoji: 🫶 heart hands - warm gratitude, chosen not default.
EMOJI = "🫶"


def main() -> None:
    assert 1 <= len(EMOJI) <= 8, "entry emoji must be 1-8 characters"
    assert EMOJI.strip(), "entry emoji must not be only whitespace"
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(EMOJI, encoding="utf-8")
    print(EMOJI)


if __name__ == "__main__":
    main()
