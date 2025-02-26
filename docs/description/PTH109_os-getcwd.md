# os-getcwd (PTH109)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.getcwd and os.getcwdb.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os. When possible, using Path object
methods such as Path.cwd() can improve readability over the os
module's counterparts (e.g., os.getcwd()).
## Examples
```
import os
cwd = os.getcwd()
```
## Use instead:
```
from pathlib import Path
cwd = Path.cwd()
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```