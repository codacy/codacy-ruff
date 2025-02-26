# expr-and-not-expr (SIM220)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for and expressions that include both an expression and its
negation.
## Why is this bad?
An and expression that includes both an expression and its negation will
always evaluate to False.
## Example
```
x and not x
```