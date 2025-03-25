# non-pep646-unpack (UP044)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for uses of Unpack[] on Python 3.11 and above, and suggests
using * instead.
## Why is this bad?
PEP 646 introduced a new syntax for unpacking sequences based on the *
operator. This syntax is more concise and readable than the previous
Unpack[] syntax.
## Example
```
from typing import Unpack
def foo(*args: Unpack[tuple[int, ...]]) -> None:
    pass
```
## Use instead:
```
def foo(*args: *tuple[int, ...]) -> None:
    pass
Fix safety
This rule's fix is marked as unsafe, as Unpack[T] and *T are considered
different values when introspecting types at runtime. However, in most cases,
the fix should be safe to apply.
```