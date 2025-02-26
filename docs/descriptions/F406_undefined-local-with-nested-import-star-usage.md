# undefined-local-with-nested-import-star-usage (F406)
Derived from the Pyflakes linter.
## What it does
Check for the use of wildcard imports outside of the module namespace.
## Why is this bad?
The use of wildcard imports outside of the module namespace (e.g., within
functions) can lead to confusion, as the import can shadow local variables.
Though wildcard imports are discouraged by PEP 8, when necessary, they
should be placed in the module namespace (i.e., at the top-level of a
module).
## Example
```
def foo():
    from math import *
```
## Use instead:
```
from math import *
def foo(): ...
```