# os-mkdir (PTH102)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.mkdir.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os. When possible, using Path object
methods such as Path.mkdir() can improve readability over the os
module's counterparts (e.g., os.mkdir()).
## Examples
```
import os
os.mkdir("./directory/")
```
## Use instead:
```
from pathlib import Path
Path("./directory/").mkdir()
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```