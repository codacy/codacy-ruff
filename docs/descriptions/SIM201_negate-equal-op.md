# negate-equal-op (SIM201)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for negated == operators.
## Why is this bad?
Negated == operators are less readable than != operators. When testing
for non-equality, it is more common to use != than ==.
## Example
```
not a == b
```
## Use instead:
```
a != b
Fix safety
The fix is marked as unsafe, as it might change the behaviour
if a and/or b overrides __eq__/__ne__
in such a manner that they don't return booleans.
```