# pandas-use-of-dot-pivot-or-unstack (PD010)
Derived from the pandas-vet linter.
## What it does
Checks for uses of .pivot or .unstack on Pandas objects.
## Why is this bad?
Prefer .pivot_table to .pivot or .unstack. .pivot_table is more general
and can be used to implement the same behavior as .pivot and .unstack.
## Example
```
import pandas as pd
df = pd.read_csv("cities.csv")
df.pivot(index="city", columns="year", values="population")
```
## Use instead:
```
import pandas as pd
df = pd.read_csv("cities.csv")
df.pivot_table(index="city", columns="year", values="population")
```