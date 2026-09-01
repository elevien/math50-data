# math50-data

Curated datasets for [Math 50](https://github.com/elevien/math50_sandbox) (Dartmouth), collected in one place so every unit, notebook, and assignment points at the same URL instead of five different external sites.

## Loading a dataset in Colab

Every dataset lives as a CSV in `data/`, so it loads with a plain `pandas.read_csv` call and a raw GitHub URL — no auth, no package install, no Drive mounting:

```python
import pandas as pd

url = "https://raw.githubusercontent.com/elevien/math50-data/main/data/<name>.csv"
df = pd.read_csv(url)
```

If you want a one-line shorthand instead, paste this into a notebook cell once:

```python
import pandas as pd

def load(name):
    """Load a math50-data dataset by name, e.g. load('kidiq')."""
    return pd.read_csv(f"https://raw.githubusercontent.com/elevien/math50-data/main/data/{name}.csv")

df = load("kidiq")
```

See [`datasets.md`](datasets.md) for the full catalog of what's available, where it came from, and how to cite it.

## Repo layout

```
data/       curated CSVs — the thing notebooks actually load
scripts/    small, one-file-per-dataset scripts that (re)produce each CSV in data/ from its original source
datasets.md catalog: name, description, source, license/citation, which units use it
```

## Adding a dataset

1. Write `scripts/prepare_<name>.py` that downloads the data from its original source and does whatever light cleaning is needed (renaming columns, dropping junk rows, fixing types) — see `scripts/prepare_template.py`. Keep processing minimal: this repo hosts data, it isn't a preprocessing pipeline. Save the result to `data/<name>.csv`.
2. Run the script to generate `data/<name>.csv`.
3. Add a row to `datasets.md` with the dataset's description, original source, and license/citation.
4. Commit both the script and the resulting CSV, so the data is reproducible from source and immediately usable without re-running anything.

## Why a separate repo

This is intentionally split from the [course-material repo](https://github.com/elevien/math50_sandbox) — data changes on a different cadence than notes and slides, shouldn't bloat that repo's history with CSVs, and is useful to point at independent of which year's course is running.
