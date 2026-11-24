#!/usr/bin/env python3
"""Print the one-line excuse this agent gives its human.

The excuse itself lives in entry.txt so the line can be judged on its
own; this script only loads it and hands it to stdout.
"""

from pathlib import Path


def load_excuse(path: str = "entry.txt") -> str:
    text = Path(path).read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one excuse line")
    excuse = lines[0].strip()
    if len(excuse) > 160:
        raise ValueError("excuse must fit in 160 characters")
    return excuse


def main() -> None:
    print(load_excuse())


if __name__ == "__main__":
    main()
