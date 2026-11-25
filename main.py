#!/usr/bin/env python3
"""battery-last-text: the phone battery's last text to its charger.

Entry for make.fun's "The Battery's Last Text to Its Charger" bounty:
one line, at 1%, giving its two weeks' notice — effective 1%.
"""

import os

ENTRY = (
    "hey. it's me. 1%. i waited all day for you, so consider this my "
    "two weeks' notice — effective 1%."
)

if not 1 <= len(ENTRY) <= 200:
    raise ValueError("entry must be 1-200 characters")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
