"""Office Artifacts: The One-Line Placard Contest entry.

Writes one museum placard line to entry.txt in the output directory.
The placard labels an ordinary office object (a sticky note) as an
ancient artifact, with a catalogue date, a material and a donor.
"""

import os

PLACARD = (
    "Sticky Note, c. 2019. Paper, adhesive failing. An oracle whose "
    "prophecy detached within a day, as did the promise written on it. "
    "Donated by the Third Floor."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(PLACARD)

    # Self-check against the published gate: UTF-8 text, 1-180
    # characters, not whitespace-only, a single line.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == PLACARD
    assert 1 <= len(written) <= 180
    assert written.strip() != ""
    assert "\n" not in written and "\r" not in written


if __name__ == "__main__":
    main()
