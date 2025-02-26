# banned-import-from (ICN003)
Derived from the flake8-import-conventions linter.
## What it does
Checks for member imports that should instead be accessed by importing the
module.
## Why is this bad?
Consistency is good. Use a common convention for imports to make your code
more readable and idiomatic.
For example, it's common to import pandas as pd, and then access
members like Series via pd.Series, rather than importing Series
directly.
## Example
```
from pandas import Series
```
## Use instead:
```
import pandas as pd
pd.Series
```