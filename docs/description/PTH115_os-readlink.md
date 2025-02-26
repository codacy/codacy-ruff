# os-readlink (PTH115)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of os.readlink.
## Why is this bad?
pathlib offers a high-level API for path manipulation, as compared to
the lower-level API offered by os. When possible, using Path object
methods such as Path.readlink() can improve readability over the os
module's counterparts (e.g., os.readlink()).
## Examples
```
import os
os.readlink(file_name)
```
## Use instead:
```
from pathlib import Path
Path(file_name).readlink()
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.
```