# pandas-use-of-dot-ix (PD007)
Derived from the pandas-vet linter.
## What it does
Checks for uses of .ix on Pandas objects.
## Why is this bad?
The .ix method is deprecated as its behavior is ambiguous. Specifically,
it's often unclear whether .ix is indexing by label or by ordinal position.
Instead, prefer the .loc method for label-based indexing, and .iloc for
ordinal indexing.
## Example
```
import pandas as pd
students_df = pd.read_csv("students.csv")
students_df.ix[0]  # 0th row or row with label 0?
```
## Use instead:
```
import pandas as pd
students_df = pd.read_csv("students.csv")
students_df.iloc[0]  # 0th row.
```