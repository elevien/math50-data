#!/usr/bin/env python3
"""Daily reported Russian personnel losses in the Ukraine war, from
PetroIvaniuk/2022-Ukraine-Russia-War-Dataset (itself compiled from the
Ukrainian General Staff's daily reports).

Used in math50_sandbox/assignment2 (casualty-statistics assignment).
"""

import pandas as pd

SOURCE_URL = (
    "https://raw.githubusercontent.com/PetroIvaniuk/"
    "2022-Ukraine-Russia-War-Dataset/main/data/russia_losses_personnel.json"
)
OUTPUT_PATH = "data/ukraine-personnel-losses.csv"


def main():
    df = pd.read_json(SOURCE_URL)
    df = df.sort_values("date")
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
