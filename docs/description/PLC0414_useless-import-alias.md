# useless-import-alias (PLC0414)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for import aliases that do not rename the original package.
In preview this rule does not apply in __init__.py files.
## Why is this bad?
The import alias is redundant and should be removed to avoid confusion.
Fix safety
This fix is marked as always unsafe because the user may be intentionally
re-exporting the import. While statements like import numpy as numpy
appear redundant, they can have semantic meaning in certain contexts.
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