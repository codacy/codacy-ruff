# pandas-df-variable-name (PD901)
Derived from the pandas-vet linter.
## What it does
Checks for assignments to the variable df.
## Why is this bad?
Although df is a common variable name for a Pandas DataFrame, it's not a
great variable name for production code, as it's non-descriptive and
prone to name conflicts.
Instead, use a more descriptive variable name.
## Example
```
import pandas as pd
df = pd.read_csv("animals.csv")
```
## Use instead:
```
import pandas as pd
animals = pd.read_csv("animals.csv")
```