# unprefixed-type-param (PYI001)
Derived from the flake8-pyi linter.
## What it does
Checks that type TypeVars, ParamSpecs, and TypeVarTuples in stubs
have names prefixed with _.
## Why is this bad?
Prefixing type parameters with _ avoids accidentally exposing names
internal to the stub.
## Example
```
from typing import TypeVar
T = TypeVar("T")
```
## Use instead:
```
from typing import TypeVar
_T = TypeVar("_T")
```