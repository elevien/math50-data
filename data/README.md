# data/

Curated, ready-to-load CSVs. Each file here should be produced by a corresponding `scripts/prepare_<name>.py` and listed in `../datasets.md`.

Load any file directly in Colab:

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/elevien/math50-data/main/data/<name>.csv")
```
