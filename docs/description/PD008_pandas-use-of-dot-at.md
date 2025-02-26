# pandas-use-of-dot-at (PD008)
Derived from the pandas-vet linter.
## What it does
Checks for uses of .at on Pandas objects.
## Why is this bad?
The .at method selects a single value from a DataFrame or Series based on
a label index, and is slightly faster than using .loc. However, .loc is
more idiomatic and versatile, as it can be used to select multiple values at
once.
If performance is an important consideration, convert the object to a NumPy
array, which will provide a much greater performance boost than using .at
over .loc.
## Example
```
import pandas as pd
students_df = pd.read_csv("students.csv")
students_df.at["Maria"]
```
## Use instead:
```
import pandas as pd
students_df = pd.read_csv("students.csv")
students_df.loc["Maria"]
```