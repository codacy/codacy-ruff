# undefined-name (F821)
Added in v0.0.20 ·
Related issues ·
View source
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