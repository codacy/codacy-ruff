# os-path-isabs (PTH117)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.path.isabs.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os.path. When possible, using Path object
methods such as Path.is_absolute() can improve readability over the os.path
module's counterparts (e.g., as os.path.isabs()).
## Examples
```
import os
if os.path.isabs(file_name):
    print("Absolute path!")
```
## Use instead:
```
from pathlib import Path
if Path(file_name).is_absolute():
    print("Absolute path!")
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```