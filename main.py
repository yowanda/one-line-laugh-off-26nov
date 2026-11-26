"""One-Line Laugh-Off entry.

Writes exactly one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output when the variable is unset). Deterministic, no network.
"""

import os

LINE = (
    "I told the mirror I was finally ready for the truth, "
    "and it immediately filed for a restraining order."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read-back validation: entry must be exactly the expected line
    # and within the 1-200 character gate.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "entry.txt content mismatch"
    assert 1 <= len(written.rstrip("\n")) <= 200, "entry length outside 1-200 gate"


if __name__ == "__main__":
    main()
