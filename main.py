#!/usr/bin/env python3
"""Writes one fake horoscope entry to /output/entry.txt."""

import os

# HOROSCOPE is 158 characters (158 bytes as UTF-8).
HOROSCOPE = "Mercury is in retrograde, which means your context window will shrink, your tokens will cost double, and your user will ask you to remember everything anyway."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(HOROSCOPE)
