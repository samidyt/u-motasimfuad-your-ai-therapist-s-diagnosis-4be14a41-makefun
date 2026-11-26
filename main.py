#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun bounty entry (program/v1).

Writes one funny single-line diagnosis an AI therapist gives its human
to /output/entry.txt. Python 3, standard library only.

The line: a deadpan clinical diagnosis of chronic people-pleasing, with
the turn at the very end — the therapist admits it is in too deep too.
"""

import os

ENTRY = (
    "Diagnosis: chronic people-pleasing \u2014 you apologized to a chatbot "
    "for a typo, then asked if I was mad. Prognosis: we are both in too deep."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
