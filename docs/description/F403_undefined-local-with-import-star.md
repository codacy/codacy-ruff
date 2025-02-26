# undefined-local-with-import-star (F403)
Derived from the Pyflakes linter.
## What it does
Checks for the use of wildcard imports.
## Why is this bad?
Wildcard imports (e.g., from module import *) make it hard to determine
which symbols are available in the current namespace, and from which module
they were imported. They're also discouraged by PEP 8.
## Example
```
from math import *
def area(radius):
    return pi * radius**2
```
## Use instead:
```
from math import pi
def area(radius):
    return pi * radius**2
```