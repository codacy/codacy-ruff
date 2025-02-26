# useless-import-alias (PLC0414)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for import aliases that do not rename the original package.
## Why is this bad?
The import alias is redundant and should be removed to avoid confusion.
## Example
```
import numpy as numpy
```
## Use instead:
```
import numpy as np
or
import numpy
```