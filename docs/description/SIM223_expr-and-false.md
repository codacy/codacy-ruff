# expr-and-false (SIM223)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for and expressions that contain falsey values.
## Why is this bad?
If the expression is used as a condition, it can be replaced in-full with
False.
In other cases, the expression can be short-circuited to the first falsey
value.
By using False (or the first falsey value), the code is more concise
and easier to understand, since it no longer contains redundant conditions.
## Example
```
if x and [] and y:
    pass
a = x and [] and y
```
## Use instead:
```
if False:
    pass
a = x and []
```