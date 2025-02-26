# pandas-use-of-dot-values (PD011)
Derived from the pandas-vet linter.
## What it does
Checks for uses of .values on Pandas Series and Index objects.
## Why is this bad?
The .values attribute is ambiguous as its return type is unclear. As
such, it is no longer recommended by the Pandas documentation.
Instead, use .to_numpy() to return a NumPy array, or .array to return a
Pandas ExtensionArray.
## Example
```
import pandas as pd
animals = pd.read_csv("animals.csv").values  # Ambiguous.
```
## Use instead:
```
import pandas as pd
animals = pd.read_csv("animals.csv").to_numpy()  # Explicit.
```