# compare-with-tuple (SIM109)
Added in v0.0.213 ·
Related issues ·
View source
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
Fix safety
This fix is always unsafe. It may change the value of the expression if any of the
comparators have side effects, and, for expressions that mix equality comparisons with
other operands, it can change the order in which operands are evaluated. Ruff preserves
the original order when an operand falls before or after the group of merged comparisons,
but if an unmatched operand falls between two merged comparisons (e.g. foo == x or bar or foo == y), it's moved after the merged in comparison.
```