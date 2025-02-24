# type-param-name-mismatch (PLC0132)
Derived from the Pylint linter.
## What it does
Checks for TypeVar, TypeVarTuple, ParamSpec, and NewType
definitions in which the name of the type parameter does not match the name
of the variable to which it is assigned.
## Why is this bad?
When defining a TypeVar or a related type parameter, Python allows you to
provide a name for the type parameter. According to PEP 484, the name
provided to the TypeVar constructor must be equal to the name of the
variable to which it is assigned.
## Example
```
from typing import TypeVar
T = TypeVar("U")
```
## Use instead:
```
from typing import TypeVar
T = TypeVar("T")
```