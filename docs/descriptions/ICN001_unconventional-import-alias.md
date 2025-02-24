# unconventional-import-alias (ICN001)
Derived from the flake8-import-conventions linter.
Fix is sometimes available.
## What it does
Checks for imports that are typically imported using a common convention,
like import pandas as pd, and enforces that convention.
## Why is this bad?
Consistency is good. Use a common convention for imports to make your code
more readable and idiomatic.
For example, import pandas as pd is a common
convention for importing the pandas library, and users typically expect
Pandas to be aliased as pd.
## Example
```
import pandas
```
## Use instead:
```
import pandas as pd
```