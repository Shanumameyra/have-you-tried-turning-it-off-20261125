#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt (the judge's gate requires
UTF-8 text of 1 to 199 characters, not only whitespace).
"""

import os

# The judge reads /output/entry.txt and requires 1-199 characters of UTF-8
# text; this line is 146 characters.
MAX_CHARS = 199

LINE = (
    "Have you tried turning it off and on again? "
    "The manual's step two is just a drawing of a man shrugging, sir, "
    "and step three is me, doing the same."
)


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1-199 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
