# if-expr-with-twisted-arms (SIM212)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for if expressions that check against a negated condition.
## Why is this bad?
if expressions that check against a negated condition are more difficult
to read than if expressions that check against the condition directly.
## Example
```
b if not a else a
```
## Use instead:
```
a if a else b
```