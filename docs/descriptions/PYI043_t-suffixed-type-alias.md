# t-suffixed-type-alias (PYI043)
Derived from the flake8-pyi linter.
## What it does
Checks for private type alias definitions suffixed with 'T'.
## Why is this bad?
It's conventional to use the 'T' suffix for type variables; the use of
such a suffix implies that the object is a TypeVar.
Adding the 'T' suffix to a non-TypeVar, it can be misleading and should
be avoided.
## Example
```
from typing import TypeAlias
_MyTypeT: TypeAlias = int
```
## Use instead:
```
from typing import TypeAlias
_MyType: TypeAlias = int
```