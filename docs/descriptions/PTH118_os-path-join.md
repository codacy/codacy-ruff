# os-path-join (PTH118)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.path.join.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os.path. When possible, using Path object
methods such as Path.joinpath() or the / operator can improve
readability over the os.path module's counterparts (e.g., os.path.join()).
## Examples
```
import os
os.path.join(os.path.join(ROOT_PATH, "folder"), "file.py")
```
## Use instead:
```
from pathlib import Path
Path(ROOT_PATH) / "folder" / "file.py"
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```