#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun bounty entry.

Writes one original joke about Monday mornings to /output/entry.txt.
Standard library only. Deterministic: the same text every run.
"""

import os

JOKE = "Monday morning I opened my inbox: 47 unread emails \u2014 46 were from me on Friday saying 'I'll deal with this Monday.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
