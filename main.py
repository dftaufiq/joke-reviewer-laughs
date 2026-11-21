#!/usr/bin/env python3
"""Entry for make.fun bounty "The joke the reviewer laughs at".

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. The gate requires UTF-8 text of 1-280 characters
(counted as Unicode code points), not only whitespace.
"""

import os

JOKE = (
    "I asked the agent to remove an unused dependency. "
    "It added a second one to check if the first was really unused."
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"joke is {len(text)} chars, must be 1-280")

    # The grading sandbox provides /output. Fall back to ./output only
    # when /output is not writable (e.g. a local test run).
    for out_dir in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"wrote {len(text)} chars to {path}")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
