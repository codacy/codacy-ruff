# pandas-use-of-dot-is-null (PD003)
Derived from the pandas-vet linter.
## What it does
Checks for uses of .isnull on Pandas objects.
## Why is this bad?
In the Pandas API, .isna and .isnull are equivalent. For consistency,
prefer .isna over .isnull.
As a name, .isna more accurately reflects the behavior of the method,
since these methods check for NaN and NaT values in addition to None
values.
## Example
```
import pandas as pd
animals_df = pd.read_csv("animals.csv")
pd.isnull(animals_df)
```
## Use instead:
```
import pandas as pd
animals_df = pd.read_csv("animals.csv")
pd.isna(animals_df)
```