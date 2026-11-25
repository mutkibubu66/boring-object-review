#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

A coaster: the dullest everyday object in the house. It does one job -
sit under a drink and stop rings - and still gets blamed when a ring
appears. One line, under 200 characters, written to /output/entry.txt.
Pure standard library.
"""

import os

OBJECT = "coaster"


def build_line() -> str:
    """One true, funny line about the coaster.

    The joke is the object's own job turned against it: a coaster exists
    to stop rings, so being blamed for a ring is the one failure it was
    hired to prevent. Keep it one sentence, no filler, so the turn
    lands in the first read.
    """
    return (
        "The coaster's job is to sit under a drink and get blamed "
        "for the ring it was hired to prevent."
    )


LINE = build_line()


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, a single line with no trailing newline.
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
