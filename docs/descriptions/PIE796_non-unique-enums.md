# non-unique-enums (PIE796)
Derived from the flake8-pie linter.
## What it does
Checks for enums that contain duplicate values.
## Why is this bad?
Enum values should be unique. Non-unique values are redundant and likely a
mistake.
## Example
```
from enum import Enum
class Foo(Enum):
    A = 1
    B = 2
    C = 1
```
## Use instead:
```
from enum import Enum
class Foo(Enum):
    A = 1
    B = 2
    C = 3
```