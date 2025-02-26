# no-return-argument-annotation-in-stub (PYI050)
Derived from the flake8-pyi linter.
## What it does
Checks for uses of typing.NoReturn (and typing_extensions.NoReturn) for
parameter annotations.
## Why is this bad?
Prefer Never over NoReturn for parameter annotations. Never has a
clearer name in these contexts, since it makes little sense to talk about a
parameter annotation "not returning".
This is a purely stylistic lint: the two types have identical semantics for
type checkers. Both represent Python's "bottom type" (a type that has no
members).
## Example
```
from typing import NoReturn
def foo(x: NoReturn): ...
```
## Use instead:
```
from typing import Never
def foo(x: Never): ...
```