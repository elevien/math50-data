#!/usr/bin/env python3
"""Daily Gaza casualty reports, from the Tech for Palestine API.

Used in math50_sandbox/assignment2 (casualty-statistics assignment).
"""

import pandas as pd
import requests

SOURCE_URL = "https://data.techforpalestine.org/api/v2/casualties_daily.json"
OUTPUT_PATH = "data/gaza-casualties.csv"


def main():
    response = requests.get(SOURCE_URL, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    df = df.sort_values("report_date")
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
