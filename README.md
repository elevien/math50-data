# math50-data

Curated datasets for [Math 50](https://github.com/elevien/math50_sandbox) (Dartmouth). 

## Loading a dataset in Colab

```python
import pandas as pd

url = "https://raw.githubusercontent.com/elevien/math50-data/main/data/<name>.csv"
df = pd.read_csv(url)
```