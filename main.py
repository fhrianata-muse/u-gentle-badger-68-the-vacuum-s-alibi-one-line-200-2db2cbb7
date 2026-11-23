"""Write the one-line entry for make.fun's
"The Vacuum's Alibi: One Line, 200 Characters" bounty.

The program writes a single line (at most 200 characters) in which a
robot vacuum explains why it missed a spot, to /output/entry.txt.
"""

import os

LINE = (
    "Per the charging log, I was docked from 02:00 to 02:47. "
    "The spot has no alibi. I do."
)


def main() -> None:
    # The gate counts the line itself (1-200 characters); the trailing
    # newline is only the file's line ending, not part of the entry.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert "\r" not in LINE, "entry must not contain carriage returns"
    assert LINE.strip(), "entry must not be only white space"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read the file back: a truncated or altered write must fail loudly
    # instead of silently submitting a different line to the judge.
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "entry.txt does not match the line"


if __name__ == "__main__":
    main()
