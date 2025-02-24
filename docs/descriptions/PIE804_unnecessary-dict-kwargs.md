# unnecessary-dict-kwargs (PIE804)
Derived from the flake8-pie linter.
Fix is sometimes available.
## What it does
Checks for unnecessary dict kwargs.
## Why is this bad?
If the dict keys are valid identifiers, they can be passed as keyword
arguments directly.
## Example
```
def foo(bar):
    return bar + 1
print(foo(**{"bar": 2}))  # prints 3
```
## Use instead:
```
def foo(bar):
    return bar + 1
print(foo(bar=2))  # prints 3
```