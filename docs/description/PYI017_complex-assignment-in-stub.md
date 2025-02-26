# complex-assignment-in-stub (PYI017)
Derived from the flake8-pyi linter.
## What it does
Checks for assignments with multiple or non-name targets in stub files.
## Why is this bad?
In general, stub files should be thought of as "data files" for a type
checker, and are not intended to be executed. As such, it's useful to
enforce that only a subset of Python syntax is allowed in a stub file, to
ensure that everything in the stub is unambiguous for the type checker.
The need to perform multi-assignment, or assignment to a non-name target,
likely indicates a misunderstanding of how stub files are intended to be
used.
## Example
```
from typing import TypeAlias
a = b = int
class Klass: ...
Klass.X: TypeAlias = int
```
## Use instead:
```
from typing import TypeAlias
a: TypeAlias = int
b: TypeAlias = int
class Klass:
    X: TypeAlias = int
```