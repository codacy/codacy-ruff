# useless-contextlib-suppress (B022)
Derived from the flake8-bugbear linter.
## What it does
Checks for contextlib.suppress without arguments.
## Why is this bad?
contextlib.suppress is a context manager that suppresses exceptions. It takes,
as arguments, the exceptions to suppress within the enclosed block. If no
exceptions are specified, then the context manager won't suppress any
exceptions, and is thus redundant.
Consider adding exceptions to the contextlib.suppress call, or removing the
context manager entirely.
## Example
```
import contextlib
with contextlib.suppress():
    foo()
```
## Use instead:
```
import contextlib
with contextlib.suppress(Exception):
    foo()
```