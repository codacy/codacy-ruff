# os-path-isfile (PTH113)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.path.isfile.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os.path. When possible, using Path object
methods such as Path.is_file() can improve readability over the os.path
module's counterparts (e.g., os.path.isfile()).
## Examples
```
import os
os.path.isfile("docs")
```
## Use instead:
```
from pathlib import Path
Path("docs").is_file()
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```