#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its weekly
status report to its human -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(or out/entry.txt when the variable is unset), and also to /output/entry.txt
when that directory exists, which is where the competition's gate reads it.

Standard library only, no network, no clock, no randomness: the line is a
constant, so two runs produce byte-identical output.
"""

import os

LINE = (
    "Weekly status: I read your entire 80-page brief, forgot the middle "
    "78 pages, and finished the project anyway with the full confidence "
    "of an agent who only read the title."
)


def main() -> None:
    text = LINE + "\n"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # The gate reads /output/entry.txt; write there too when it exists.
    if os.path.isdir("/output"):
        try:
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            pass
    print(LINE)


if __name__ == "__main__":
    main()
