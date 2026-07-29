# unnecessary-assign (RET504)
Added in v0.0.154 ·
Related issues ·
View source
Derived from the flake8-return linter.
Fix is always available.
## What it does
Checks for variable assignments that immediately precede a return of the
assigned variable.
## Why is this bad?
The variable assignment is not necessary, as the value can be returned
directly.
## Example
```
def foo():
    bar = 1
    return bar
```
## Use instead:
```
def foo():
    return 1
```