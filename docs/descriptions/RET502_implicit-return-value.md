# implicit-return-value (RET502)
Derived from the flake8-return linter.
Fix is always available.
## What it does
Checks for the presence of a return statement with no explicit value,
for functions that return non-None values elsewhere.
## Why is this bad?
Including a return statement with no explicit value can cause confusion
when other return statements in the function return non-None values.
Python implicitly assumes return None if no other return value is present.
Adding an explicit return None can make the code more readable by clarifying
intent.
## Example
```
def foo(bar):
    if not bar:
        return
    return 1
```
## Use instead:
```
def foo(bar):
    if not bar:
        return None
    return 1
```