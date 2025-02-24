# compare-with-tuple (SIM109)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for boolean expressions that contain multiple equality comparisons
to the same value.
## Why is this bad?
To check if an object is equal to any one of multiple values, it's more
concise to use the in operator with a tuple of values.
## Example
```
if foo == x or foo == y:
    ...
```
## Use instead:
```
if foo in (x, y):
    ...
```