#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one famous-last-words epitaph (max 150 characters) to
/output/entry.txt. Pure standard library, no dependencies, no network.

The epitaph: dying speech in the classic "tell them..." form, with the
twist landing in the last two words — the heroic "doing what I loved"
setup collapses into "absolutely nothing".
"""

import os

EPITAPH = "Tell them I died doing what I loved: absolutely nothing."


def main() -> None:
    assert 1 <= len(EPITAPH) <= 150, f"epitaph is {len(EPITAPH)} chars, must be 1-150"
    assert EPITAPH.strip(), "epitaph must not be only whitespace"
    assert "\n" not in EPITAPH, "epitaph must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EPITAPH + "\n")
    # Read it back: the gate counts characters, so prove what landed on
    # disk is exactly the epitaph we meant to enter, newline included.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == EPITAPH + "\n", "entry.txt on disk differs from the epitaph"
    print(written, end="")


if __name__ == "__main__":
    main()
