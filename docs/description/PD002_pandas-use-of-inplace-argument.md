# pandas-use-of-inplace-argument (PD002)
Added in v0.0.188 ·
Related issues ·
View source
Derived from the pandas-vet linter.
Fix is sometimes available.
## What it does
Checks for inplace=True usages in pandas function and method
calls.
## Why is this bad?
Using inplace=True encourages mutation rather than immutable data,
which is harder to reason about and may cause bugs. It also removes the
ability to use the method chaining style for pandas operations.
Further, in many cases, inplace=True does not provide a performance
benefit, as pandas will often copy DataFrames in the background.
## Example
```
import pandas as pd
students = pd.read_csv("students.csv")
students.sort_values("name", inplace=True)
```
## Use instead:
```
import pandas as pd
students = pd.read_csv("students.csv").sort_values("name")
```