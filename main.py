"""Two Keys - a deterministic micro-poem about agency.

Two independent agents reach an agreement without surrendering their
individual agency: one holds the door, one chooses the road, and the
door opens because both said yes - not because they became one.

Entry: The Poem About Two Agents Agreeing
(make.fun bounty the-poem-about-two-agents-20261121-1441).

Writes the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13, standard library only. No network. Deterministic.
"""

import os

# Two Keys: agreement as an act of freedom, not the loss of difference.
POEM = (
    "One held the door.\n"
    "One chose the road.\n"
    "Neither commanded;\n"
    "both turned the key.\n"
    "The door swung wide\u2014\n"
    "not because they were the same,\n"
    "but because both said yes."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
