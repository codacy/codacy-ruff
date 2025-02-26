# builtin-open (PTH123)
Derived from the flake8-use-pathlib linter.
## What it does
Checks for uses of the open() builtin.
## Why is this bad?
pathlib offers a high-level API for path manipulation. When possible,
using Path object methods such as Path.open() can improve readability
over the open builtin.
## Examples
```
with open("f1.py", "wb") as fp:
    ...
```
## Use instead:
```
from pathlib import Path
with Path("f1.py").open("wb") as fp:
    ...
Known issues
While using pathlib can improve the readability and type safety of your code,
it can be less performant than working directly with strings,
especially on older versions of Python.
```