# expr-or-true (SIM222)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for or expressions that contain truthy values.
## Why is this bad?
If the expression is used as a condition, it can be replaced in-full with
True.
In other cases, the expression can be short-circuited to the first truthy
value.
By using True (or the first truthy value), the code is more concise
and easier to understand, since it no longer contains redundant conditions.
## Example
```
if x or [1] or y:
    pass
a = x or [1] or y
```
## Use instead:
```
if True:
    pass
a = x or [1]
```