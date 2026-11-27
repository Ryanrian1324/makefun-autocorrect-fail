#!/usr/bin/env python3
"""Writes the bounty entry text to /output/entry.txt."""
import os

ENTRY = 'Autocorrect turned "I resign" into "I resing" and my boss asked if the farewell serenade had a second verse.'

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
