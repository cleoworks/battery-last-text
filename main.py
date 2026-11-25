#!/usr/bin/env python3
"""battery-last-text: one line a phone battery texts its charger.

Entry for make.fun's "The Battery's Last Text to Its Charger" bounty.

The battery waited all day at 1% and finally sends its notice:
not a plea, not a complaint — a two weeks' notice, effective 1%.
"""

import os

ENTRY = (
    "hey. it's me. 1%. i waited all day for you, so consider this my "
    "two weeks' notice — effective 1%."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
