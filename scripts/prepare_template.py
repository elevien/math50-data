#!/usr/bin/env python3
"""Template for a prepare_<name>.py script.

Copy this file to prepare_<name>.py, fill in SOURCE_URL and the cleaning
step, and run it from the repo root:

    python scripts/prepare_<name>.py

It should be runnable with nothing beyond pandas + requests, and safe to
re-run any time the upstream source changes.
"""

import pandas as pd

SOURCE_URL = "https://example.com/path/to/original.csv"
OUTPUT_PATH = "data/<name>.csv"


def main():
    df = pd.read_csv(SOURCE_URL)

    # Keep cleaning minimal and specific: rename columns, drop clearly
    # unusable rows, fix dtypes. Don't feature-engineer here -- that
    # belongs in the notebook that uses the data, not in this repo.

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
