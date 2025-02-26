# pandas-use-of-dot-read-table (PD012)
Derived from the pandas-vet linter.
## What it does
Checks for uses of pd.read_table to read CSV files.
## Why is this bad?
In the Pandas API, pd.read_csv and pd.read_table are equivalent apart
from their default separator: pd.read_csv defaults to a comma (,),
while pd.read_table defaults to a tab (\t) as the default separator.
Prefer pd.read_csv over pd.read_table when reading comma-separated
data (like CSV files), as it is more idiomatic.
## Example
```
import pandas as pd
cities_df = pd.read_table("cities.csv", sep=",")
```
## Use instead:
```
import pandas as pd
cities_df = pd.read_csv("cities.csv")
```