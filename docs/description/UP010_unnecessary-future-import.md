# unnecessary-future-import (UP010)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for unnecessary __future__ imports.
## Why is this bad?
The __future__ module is used to enable features that are not yet
available in the current Python version. If a feature is already
available in the minimum supported Python version, importing it
from __future__ is unnecessary and should be removed to avoid
confusion.
## Example
```
from __future__ import print_function
print("Hello, world!")
```
## Use instead:
```
print("Hello, world!")
```