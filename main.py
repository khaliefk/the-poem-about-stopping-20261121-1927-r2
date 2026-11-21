#!/usr/bin/env python3
"""Write one short poem about stopping to /output/entry.txt."""

import os

POEM = """The hand lifts, then learns to rest.
The door you meant to open stays shut —
not locked, just held, by a palm that knows
the next step can wait.
Nothing here is taken from you.
The key stays in your pocket,
warm as a kept word.
"""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
