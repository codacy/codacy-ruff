# negate-not-equal-op (SIM202)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for negated != operators.
## Why is this bad?
Negated != operators are less readable than == operators, as they avoid a
double negation.
## Example
```
not a != b
```
## Use instead:
```
a == b
Fix safety
The fix is marked as unsafe, as it might change the behaviour
if a and/or b overrides __ne__/__eq__
in such a manner that they don't return booleans.
```