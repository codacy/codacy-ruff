# expr-or-not-expr (SIM221)
Added in v0.0.211 ·
Related issues ·
View source
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for or expressions that include both an expression and its
negation.
## Why is this bad?
An or expression that includes both an expression and its negation will
always evaluate to True.
## Example
```
x or not x
```