# path-constructor-current-directory (PTH201)
Derived from the flake8-use-pathlib linter.
Fix is always available.
## What it does
Checks for pathlib.Path objects that are initialized with the current
directory.
## Why is this bad?
The Path() constructor defaults to the current directory, so passing it
in explicitly (as ".") is unnecessary.
## Example
```
from pathlib import Path
_ = Path(".")
```
## Use instead:
```
from pathlib import Path
_ = Path()
```