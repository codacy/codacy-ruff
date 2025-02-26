# os-path-expanduser (PTH111)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.path.expanduser.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os.path. When possible, using Path object
methods such as Path.expanduser() can improve readability over the os.path
module's counterparts (e.g., as os.path.expanduser()).
## Examples
```
import os
os.path.expanduser("~/films/Monty Python")
```
## Use instead:
```
from pathlib import Path
Path("~/films/Monty Python").expanduser()
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```