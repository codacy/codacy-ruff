# unnecessary-builtin-import (UP029)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for unnecessary imports of builtins.
## Why is this bad?
Builtins are always available. Importing them is unnecessary and should be
removed to avoid confusion.
## Example
```
from builtins import str
str(1)
```
## Use instead:
```
str(1)
```