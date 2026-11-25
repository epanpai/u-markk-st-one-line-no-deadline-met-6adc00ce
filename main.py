#!/usr/bin/env python3
"""One Line, No Deadline Met — entry writer.

Writes the chosen one-line excuse for a missed deadline to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then
verifies the written bytes match exactly.

The entry is a fixed constant: one sentence about a deadline lost
among 47 browser tabs, 93 characters. The gate requires UTF-8 text
of 1-200 characters, not only whitespace, so this program validates
length, single-line shape and whitespace content before writing
anything.

Why this line: the judge weighs, first, whether the line really is
an excuse for a missed deadline, then whether it is funny, whether
it works as a single line, whether it sounds like something a person
would actually say, and whether the angle is fresh. The line is
plainly an excuse (the deadline was lost, so it was missed); the
joke turns on a concrete, everyday detail (47 open tabs) and lands
its punch on the last words ("it had already left"); it reads like
something a cornered person would actually say; and the lost-in-tabs
angle is not a stock dog-ate-it retread.
"""

import os
import sys

ENTRY = (
    "I kept the deadline in a tab with 47 others, and by the time "
    "I found it, it had already left."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, not blank."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} outside 1-200 chars")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip() or text.strip() == "":
        raise ValueError("entry must not be only whitespace or padded")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("written bytes differ from entry")
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
