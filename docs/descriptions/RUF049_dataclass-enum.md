# dataclass-enum (RUF049)
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for enum classes which are also decorated with @dataclass.
## Why is this bad?
Decorating an enum with @dataclass() does not cause any errors at runtime,
but may cause erroneous results:
@dataclass
class E(Enum):
    A = 1
    B = 2
print(E.A == E.B)  # True
## Example
```
from dataclasses import dataclass
from enum import Enum
@dataclass
class E(Enum): ...
```
## Use instead:
```
from enum import Enum
class E(Enum): ...
```