#!/usr/bin/env python3
"""Writes the autocorrect-fail entry text to $OUTPUT_DIR/entry.txt (default /output)."""
import os

ENTRY = 'Autocorrect turned my resignation letter into "I resing" — HR now thinks I am the office troubadour (their words, in the all-staff) and, honestly, the demo is booked for Friday. Unplugged.'

def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
