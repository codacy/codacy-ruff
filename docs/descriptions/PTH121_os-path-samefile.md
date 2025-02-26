# os-path-samefile (PTH121)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.path.samefile.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os.path. When possible, using Path object
methods such as Path.samefile() can improve readability over the os.path
module's counterparts (e.g., os.path.samefile()).
## Examples
```
import os
os.path.samefile("f1.py", "f2.py")
```
## Use instead:
```
from pathlib import Path
Path("f1.py").samefile("f2.py")
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```