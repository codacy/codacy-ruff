# boolean-default-value-positional-argument (FBT002)
Derived from the flake8-boolean-trap linter.
## What it does
Checks for the use of boolean positional arguments in function definitions,
as determined by the presence of a boolean default value.
## Why is this bad?
Calling a function with boolean positional arguments is confusing as the
meaning of the boolean value is not clear to the caller and to future
readers of the code.
The use of a boolean will also limit the function to only two possible
behaviors, which makes the function difficult to extend in the future.
Instead, consider refactoring into separate implementations for the
True and False cases, using an Enum, or making the argument a
keyword-only argument, to force callers to be explicit when providing
the argument.
## Example
```
from math import ceil, floor
def round_number(number, up=True):
    return ceil(number) if up else floor(number)
round_number(1.5, True)  # What does `True` mean?
round_number(1.5, False)  # What does `False` mean?
Instead, refactor into separate implementations:
from math import ceil, floor
def round_up(number):
    return ceil(number)
def round_down(number):
    return floor(number)
round_up(1.5)
round_down(1.5)
Or, refactor to use an Enum:
from enum import Enum
class RoundingMethod(Enum):
    UP = 1
    DOWN = 2
def round_number(value, method):
    return ceil(number) if method is RoundingMethod.UP else floor(number)
round_number(1.5, RoundingMethod.UP)
round_number(1.5, RoundingMethod.DOWN)
Or, make the argument a keyword-only argument:
from math import ceil, floor
def round_number(number, *, up=True):
    return ceil(number) if up else floor(number)
round_number(1.5, up=True)
round_number(1.5, up=False)
```