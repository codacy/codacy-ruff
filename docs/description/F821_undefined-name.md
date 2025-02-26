# undefined-name (F821)
Derived from the Pyflakes linter.
## What it does
Checks for uses of undefined names.
## Why is this bad?
An undefined name is likely to raise NameError at runtime.
## Example
```
def double():
    return n * 2  # raises `NameError` if `n` is undefined when `double` is called
```
## Use instead:
```
def double(n):
    return n * 2
```