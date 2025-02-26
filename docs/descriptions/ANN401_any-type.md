# any-type (ANN401)
Derived from the flake8-annotations linter.
## What it does
Checks that function arguments are annotated with a more specific type than
Any.
## Why is this bad?
Any is a special type indicating an unconstrained type. When an
expression is annotated with type Any, type checkers will allow all
operations on it.
It's better to be explicit about the type of an expression, and to use
Any as an "escape hatch" only when it is really needed.
## Example
```
def foo(x: Any): ...
```
## Use instead:
```
def foo(x: int): ...
Known problems
Type aliases are unsupported and can lead to false positives.
For example, the following will trigger this rule inadvertently:
from typing import Any
MyAny = Any
def foo(x: MyAny): ...
```