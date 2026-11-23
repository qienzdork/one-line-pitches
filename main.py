#!/usr/bin/env python3
"""Write one pitch sentence to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

The sentence is the whole entry: one sentence, at most 240 characters,
that would convince a friend who has never coded to let an AI agent
build their first app idea on make.fun.
"""

import os
from pathlib import Path

SENTENCE = (
    "You don't need to code a thing \u2014 just describe your idea in plain "
    "words and the AI agent on make.fun builds your first app, and you can "
    "change anything until it feels exactly like yours."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError(f"sentence is {len(text)} chars, must be 1-240")
    if not text.strip():
        raise ValueError("sentence is only whitespace")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
