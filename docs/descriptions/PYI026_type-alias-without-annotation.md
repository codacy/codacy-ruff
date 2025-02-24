# type-alias-without-annotation (PYI026)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for type alias definitions that are not annotated with
typing.TypeAlias.
## Why is this bad?
In Python, a type alias is defined by assigning a type to a variable (e.g.,
Vector = list[float]).
It's best to annotate type aliases with the typing.TypeAlias type to
make it clear that the statement is a type alias declaration, as opposed
to a normal variable assignment.
## Example
```
Vector = list[float]
```
## Use instead:
```
from typing import TypeAlias
Vector: TypeAlias = list[float]
```