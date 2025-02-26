# redundant-literal-union (PYI051)
Derived from the flake8-pyi linter.
## What it does
Checks for redundant unions between a Literal and a builtin supertype of
that Literal.
## Why is this bad?
Using a Literal type in a union with its builtin supertype is redundant,
as the supertype will be strictly more general than the Literal type.
For example, Literal["A"] | str is equivalent to str, and
Literal[1] | int is equivalent to int, as str and int are the
supertypes of "A" and 1 respectively.
## Example
```
from typing import Literal
x: Literal["A", b"B"] | str
```
## Use instead:
```
from typing import Literal
x: Literal[b"B"] | str
```