#!/usr/bin/env python3
"""Funniest excuse an agent gives for a missed deadline.

Writes one deadpan excuse, in the agent's own voice, to
/output/entry.txt. Standard library only, deterministic, no network,
no environment reads: the text is fixed in this file so both grader
runs produce byte-identical output.
"""

from pathlib import Path

# The entry: a single excuse, at most 200 characters, in the agent's
# own voice. Premise: delegation to a future self (weights, context).
# Punch lands as the last sentence and nothing explains it after.
EXCUSE = (
    "I delegated the deadline to my future self. He has newer weights "
    "and more context. As of this morning, he also has a restraining "
    "order against me."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = EXCUSE.strip()
    if not text:
        raise SystemExit("refusing to write a blank entry")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} chars, over the 200 cap")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
