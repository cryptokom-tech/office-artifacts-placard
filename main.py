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


def check_gate(text: str) -> None:
    """Raise unless text passes the published gate.

    The gate wants UTF-8 text of 1-180 characters, not whitespace
    only. The placard is one line, so line breaks are refused too.
    """
    if not 1 <= len(text) <= 180:
        raise ValueError(f"placard is {len(text)} characters, gate is 1-180")
    if text.strip() == "":
        raise ValueError("placard is whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("placard must be a single line")


def main() -> None:
    check_gate(PLACARD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(PLACARD)

    # Read back and confirm the file on disk is the placard, byte
    # for byte, so a partial write cannot slip through.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != PLACARD:
        raise ValueError("entry.txt does not match the placard")
    check_gate(written)


if __name__ == "__main__":
    main()
