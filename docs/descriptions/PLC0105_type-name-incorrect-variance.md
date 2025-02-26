# type-name-incorrect-variance (PLC0105)
Derived from the Pylint linter.
## What it does
Checks for type names that do not match the variance of their associated
type parameter.
## Why is this bad?
PEP 484 recommends the use of the _co and _contra suffixes for
covariant and contravariant type parameters, respectively (while invariant
type parameters should not have any such suffix).
## Example
```
from typing import TypeVar
T = TypeVar("T", covariant=True)
U = TypeVar("U", contravariant=True)
V_co = TypeVar("V_co")
```
## Use instead:
```
from typing import TypeVar
T_co = TypeVar("T_co", covariant=True)
U_contra = TypeVar("U_contra", contravariant=True)
V = TypeVar("V")
```