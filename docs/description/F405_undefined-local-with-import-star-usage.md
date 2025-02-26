# undefined-local-with-import-star-usage (F405)
Derived from the Pyflakes linter.
## What it does
Checks for names that might be undefined, but may also be defined in a
wildcard import.
## Why is this bad?
Wildcard imports (e.g., from module import *) make it hard to determine
which symbols are available in the current namespace. If a module contains
a wildcard import, and a name in the current namespace has not been
explicitly defined or imported, then it's unclear whether the name is
undefined or was imported by the wildcard import.
If the name is defined in via a wildcard import, that member should be
imported explicitly to avoid confusion.
If the name is not defined in a wildcard import, it should be defined or
imported.
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