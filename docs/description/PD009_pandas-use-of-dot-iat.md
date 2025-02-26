# pandas-use-of-dot-iat (PD009)
Derived from the pandas-vet linter.
## What it does
Checks for uses of .iat on Pandas objects.
## Why is this bad?
The .iat method selects a single value from a DataFrame or Series based
on an ordinal index, and is slightly faster than using .iloc. However,
.iloc is more idiomatic and versatile, as it can be used to select
multiple values at once.
If performance is an important consideration, convert the object to a NumPy
array, which will provide a much greater performance boost than using .iat
over .iloc.
## Example
```
import pandas as pd
students_df = pd.read_csv("students.csv")
students_df.iat[0]
```
## Use instead:
```
import pandas as pd
students_df = pd.read_csv("students.csv")
students_df.iloc[0]
Or, using NumPy:
import numpy as np
import pandas as pd
students_df = pd.read_csv("students.csv")
students_df.to_numpy()[0]
```