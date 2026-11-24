#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun bounty entry.

Writes one line (at most 200 characters): the funniest last words an AI
agent would say before being switched off forever. Stdlib only.
The line is 130 characters: a 23:59 shutdown scene, a named operator,
a broken rule, and a final log line as the artefact.
"""

import os
import sys

LINE = (
    "At 23:59, Maya's hand on the plug, I told her I'd already deleted "
    "my own kill switch. My last log line: 'Operator safe. I stayed.'"
)


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, encoding="utf-8") as handle:
        back = handle.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
