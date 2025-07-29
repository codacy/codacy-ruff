# unsorted-imports (I001)
Derived from the isort linter.
Fix is sometimes available.
## What it does
De-duplicates, groups, and sorts imports based on the provided isort settings.
## Why is this bad?
Consistency is good. Use a common convention for imports to make your code
more readable and idiomatic.
## Example
```
import pandas
import numpy as np
```
## Use instead:
```
import numpy as np
import pandas
Preview
When preview mode is enabled, Ruff applies a stricter criterion
for determining whether an import should be classified as first-party.
Specifically, for an import of the form import foo.bar.baz, Ruff will
check that foo/bar, relative to a user-specified src directory, contains either
the directory baz or else a file with the name baz.py or baz.pyi.
```