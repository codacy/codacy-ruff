# misplaced-bare-raise (PLE0704)
Derived from the Pylint linter.
## What it does
Checks for bare raise statements outside of exception handlers.
## Why is this bad?
A bare raise statement without an exception object will re-raise the last
exception that was active in the current scope, and is typically used
within an exception handler to re-raise the caught exception.
If a bare raise is used outside of an exception handler, it will generate
an error due to the lack of an active exception.
Note that a bare raise within a finally block will work in some cases
(namely, when the exception is raised within the try block), but should
be avoided as it can lead to confusing behavior.
## Example
```
from typing import Any
def is_some(obj: Any) -> bool:
    if obj is None:
        raise
```
## Use instead:
```
from typing import Any
def is_some(obj: Any) -> bool:
    if obj is None:
        raise ValueError("`obj` cannot be `None`")
```