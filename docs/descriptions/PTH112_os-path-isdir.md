# os-path-isdir (PTH112)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.path.isdir.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os.path. When possible, using Path object
methods such as Path.is_dir() can improve readability over the os.path
module's counterparts (e.g., os.path.isdir()).
## Examples
```
import os
os.path.isdir("docs")
```
## Use instead:
```
from pathlib import Path
Path("docs").is_dir()
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```