# redundant-final-literal (PYI064)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for redundant Final[Literal[...]] annotations.
## Why is this bad?
All constant variables annotated as Final are understood as implicitly
having Literal types by a type checker. As such, a Final[Literal[...]]
annotation can often be replaced with a bare Final, annotation, which
will have the same meaning to the type checker while being more concise and
more readable.
## Example
```
from typing import Final, Literal
x: Final[Literal[42]]
y: Final[Literal[42]] = 42
```
## Use instead:
```
from typing import Final, Literal
x: Final = 42
y: Final = 42
```