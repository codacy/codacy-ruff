# os-chmod (PTH101)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.chmod.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os. When possible, using Path object
methods such as Path.chmod() can improve readability over the os
module's counterparts (e.g., os.chmod()).
## Examples
```
import os
os.chmod("file.py", 0o444)
```
## Use instead:
```
from pathlib import Path
Path("file.py").chmod(0o444)
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```