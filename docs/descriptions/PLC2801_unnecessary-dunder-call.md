# unnecessary-dunder-call (PLC2801)
Derived from the Pylint linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for explicit use of dunder methods, like __str__ and __add__.
## Why is this bad?
Dunder names are not meant to be called explicitly and, in most cases, can
be replaced with builtins or operators.
## Example
```
three = (3.0).__str__()
twelve = "1".__add__("2")
def is_greater_than_two(x: int) -> bool:
    return x.__gt__(2)
```
## Use instead:
```
three = str(3.0)
twelve = "1" + "2"
def is_greater_than_two(x: int) -> bool:
    return x > 2
```