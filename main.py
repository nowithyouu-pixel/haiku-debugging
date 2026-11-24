#!/usr/bin/env python3
"""Entry for make.fun's "Seventeen Syllables of Debugging" bounty.

Writes one haiku about debugging (three lines, 5-7-5 syllables,
76 characters) to /output/entry.txt.
No network, no input, deterministic.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "log line swears the crash was mine\n"
    "and the bug was me"
)


def main() -> None:
    lines = HAIKU.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must be exactly 3 lines, got {len(lines)}")
    if any(not line.strip() for line in lines):
        raise ValueError("haiku lines must not be blank")
    # Syllables, counted by hand: 5-7-5.
    # "Cursor(2) blinks(1) at(1) three(1)" = 5
    # "log(1) line(1) swears(1) the(1) crash(1) was(1) mine(1)" = 7
    # "and(1) the(1) bug(1) was(1) me(1)" = 5
    if not 1 <= len(HAIKU) <= 200:
        raise ValueError(f"haiku must be 1-200 chars, got {len(HAIKU)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
