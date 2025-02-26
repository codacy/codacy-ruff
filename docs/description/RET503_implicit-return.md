# implicit-return (RET503)
Derived from the flake8-return linter.
Fix is always available.
## What it does
Checks for missing explicit return statements at the end of functions
that can return non-None values.
## Why is this bad?
The lack of an explicit return statement at the end of a function that
can return non-None values can cause confusion. Python implicitly returns
None if no other return value is present. Adding an explicit
return None can make the code more readable by clarifying intent.
## Example
```
def foo(bar):
    if not bar:
        return 1
```
## Use instead:
```
def foo(bar):
    if not bar:
        return 1
    return None
```