# unnecessary-return-none (RET501)
Derived from the flake8-return linter.
Fix is always available.
## What it does
Checks for the presence of a return None statement when None is the only
possible return value.
## Why is this bad?
Python implicitly assumes return None if an explicit return value is
omitted. Therefore, explicitly returning None is redundant and should be
avoided when it is the only possible return value across all code paths
in a given function.
## Example
```
def foo(bar):
    if not bar:
        return
    return None
```
## Use instead:
```
def foo(bar):
    if not bar:
        return
    return
```