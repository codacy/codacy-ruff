# py-path (PTH124)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of the py.path library.
## Why is this bad?
The py.path library is in maintenance mode. Instead, prefer the standard
library's pathlib module, or third-party modules like path (formerly
py.path).
## Examples
```
import py.path
p = py.path.local("/foo/bar").join("baz/qux")
```
## Use instead:
```
from pathlib import Path
p = Path("/foo/bar") / "bar" / "qux"
```