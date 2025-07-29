# reimplemented-builtin (SIM110)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for for loops that can be replaced with a builtin function, like
any or all.
## Why is this bad?
Using a builtin function is more concise and readable.
## Example
```
def foo():
    for item in iterable:
        if predicate(item):
            return True
    return False
```
## Use instead:
```
def foo():
    return any(predicate(item) for item in iterable)
Fix safety
This fix is always marked as unsafe because it might remove comments.
```