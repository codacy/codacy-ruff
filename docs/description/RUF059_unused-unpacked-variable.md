# unused-unpacked-variable (RUF059)
Added in 0.13.0 ·
Related issues ·
View source
Fix is sometimes available.
## What it does
Checks for the presence of unused variables in unpacked assignments.
## Why is this bad?
A variable that is defined but never used can confuse readers.
If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
lint.dummy-variable-rgx pattern.
## Example
```
def get_pair():
    return 1, 2
def foo():
    x, y = get_pair()
    return x
```
## Use instead:
```
def foo():
    x, _ = get_pair()
    return x
See also
This rule applies only to unpacked assignments. For regular assignments, see
unused-variable.
```