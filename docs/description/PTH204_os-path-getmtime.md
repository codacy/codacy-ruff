# os-path-getmtime (PTH204)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.path.getmtime.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os.path.
When possible, using Path object methods such as Path.stat() can
improve readability over the os.path module's counterparts (e.g.,
os.path.getmtime()).
## Examples
```
import os
os.path.getmtime(__file__)
```
## Use instead:
```
from pathlib import Path
Path(__file__).stat().st_mtime
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```