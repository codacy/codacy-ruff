# empty-type-checking-block (TC005)
Derived from the flake8-type-checking linter.
Fix is always available.
## What it does
Checks for an empty type-checking block.
## Why is this bad?
The type-checking block does not do anything and should be removed to avoid
confusion.
## Example
```
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass
print("Hello, world!")
```
## Use instead:
```
print("Hello, world!")
```