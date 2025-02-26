# os-rmdir (PTH106)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.rmdir.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os. When possible, using Path object
methods such as Path.rmdir() can improve readability over the os
module's counterparts (e.g., os.rmdir()).
## Examples
```
import os
os.rmdir("folder/")
```
## Use instead:
```
from pathlib import Path
Path("folder/").rmdir()
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```