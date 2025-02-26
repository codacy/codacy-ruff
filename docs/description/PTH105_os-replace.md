# os-replace (PTH105)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.replace.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os. When possible, using Path object
methods such as Path.replace() can improve readability over the os
module's counterparts (e.g., os.replace()).
Note that os functions may be preferable if performance is a concern,
e.g., in hot loops.
## Examples
```
import os
os.replace("old.py", "new.py")
```
## Use instead:
```
from pathlib import Path
Path("old.py").replace("new.py")
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```