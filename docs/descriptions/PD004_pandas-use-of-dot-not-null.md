# pandas-use-of-dot-not-null (PD004)
Derived from the pandas-vet linter.
## What it does
Checks for uses of .notnull on Pandas objects.
## Why is this bad?
In the Pandas API, .notna and .notnull are equivalent. For consistency,
prefer .notna over .notnull.
As a name, .notna more accurately reflects the behavior of the method,
since these methods check for NaN and NaT values in addition to None
values.
## Example
```
import pandas as pd
animals_df = pd.read_csv("animals.csv")
pd.notnull(animals_df)
```
## Use instead:
```
import pandas as pd
animals_df = pd.read_csv("animals.csv")
pd.notna(animals_df)
```