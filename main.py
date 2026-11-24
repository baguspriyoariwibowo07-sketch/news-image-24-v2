#!/usr/bin/env python3
"""Entry point for the 24 November 2026 world-news broadsheet, v2.

The picture is drawn by draw24v2.py and committed beside this file
as entry.png. This program only copies that file into the output
directory named by MAKEFUN_OUTPUT_DIR (or ./output when the
variable is unset). Standard library only, no network and no clock,
so both graded runs write exactly the same bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        print("entry.png is missing beside main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        print("copy size mismatch", file=sys.stderr)
        return 1
    print("wrote", dest, os.path.getsize(dest), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
