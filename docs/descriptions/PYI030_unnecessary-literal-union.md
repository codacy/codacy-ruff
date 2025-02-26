# unnecessary-literal-union (PYI030)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for the presence of multiple literal types in a union.
## Why is this bad?
Literal["foo", 42] has identical semantics to
Literal["foo"] | Literal[42], but is clearer and more concise.
## Example
```
from typing import Literal
field: Literal[1] | Literal[2] | str
```
## Use instead:
```
from typing import Literal
field: Literal[1, 2] | str
```