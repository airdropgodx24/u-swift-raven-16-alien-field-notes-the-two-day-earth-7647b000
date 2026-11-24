#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

One original line of plain text: a review of planet Earth left by an
alien tourist. The program writes exactly that line to /output/entry.txt.
"""

import os

REVIEW = (
    "Humans pay to stand in line for a hot drink, then complain it's too hot, "
    "then stand in line again tomorrow. I respect the commitment. "
    "4/5 stars, would visit again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = REVIEW.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"review line must be 1-200 characters, got {len(line)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
