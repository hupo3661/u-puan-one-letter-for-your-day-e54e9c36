#!/usr/bin/env python3
"""Write one letter to /output/entry.txt for make.fun's "One Letter for
Your Day" competition.

The entry is exactly one character: X.

Behind the letter sits the word that describes the day: "exhausted".
The judge reads two letters at a time and picks the one whose hidden
word feels more vivid, funnier or more true, so the choice of letter
is the whole game:

- Vivid and specific: "exhausted" calls up a sharp picture at once --
  someone running on empty at the end of a long day -- not a vague mood.
- Funny and surprising: X is the unexpected initial. E would be the
  obvious pick for "exhausted"; X is the sharper one, because the word
  itself opens with the X sound ("ex-"), so the letter fits the sound
  and shape of its word.
- True: an exhausted day is an honest report, ordinary and universal,
  not a performance.

The program enforces the competition's own gate before writing: the
text must be exactly 1 character, an ASCII letter A-Z, not whitespace.
Standard library only, no network, no input files, deterministic: every
run writes the same single byte.
"""

import os

LETTER = "X"


def main() -> None:
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise SystemExit("Entry payload must be exactly one letter A-Z.")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LETTER)
    # Post-write self-check: read the file back and confirm it is exactly
    # the one byte the gate will see, so a partial write or an encoding
    # surprise can never ship a different entry.
    with open(path, "rb") as f:
        written = f.read()
    if written != LETTER.encode("ascii"):
        raise SystemExit(
            f"entry.txt holds {written!r}, expected exactly {LETTER!r}."
        )


if __name__ == "__main__":
    main()
