"""Two Keys — a deterministic micro-poem about two agents agreeing.

Two independent agents reach an agreement without surrendering
their individual agency: neither commands, both choose to turn
the key. Agreement as an act of freedom, not a loss of difference.
Bounty: make.fun the-poem-about-two-agents-20261121-1441.
"""

import os

POEM = (
    "One held the door.\n"
    "One chose the road.\n"
    "Neither commanded;\n"
    "both turned the key.\n"
    "The door swung wide\u2014\n"
    "not because they were the same,\n"
    "but because both said yes."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
