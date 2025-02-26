# overload-with-docstring (D418)
Derived from the pydocstyle linter.
## What it does
Checks for @overload function definitions that contain a docstring.
## Why is this bad?
The @overload decorator is used to define multiple compatible signatures
for a given function, to support type-checking. A series of @overload
definitions should be followed by a single non-decorated definition that
contains the implementation of the function.
@overload function definitions should not contain a docstring; instead,
the docstring should be placed on the non-decorated definition that contains
the implementation.
## Example
```
from typing import overload
@overload
def factorial(n: int) -> int:
    """Return the factorial of n."""
@overload
def factorial(n: float) -> float:
    """Return the factorial of n."""
def factorial(n):
    """Return the factorial of n."""
factorial.__doc__  # "Return the factorial of n."
```
## Use instead:
```
from typing import overload
@overload
def factorial(n: int) -> int: ...
@overload
def factorial(n: float) -> float: ...
def factorial(n):
    """Return the factorial of n."""
factorial.__doc__  # "Return the factorial of n."
```