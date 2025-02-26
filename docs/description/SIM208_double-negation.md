# double-negation (SIM208)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for double negations (i.e., multiple not operators).
## Why is this bad?
A double negation is redundant and less readable than omitting the not
operators entirely.
## Example
```
not (not a)
```
## Use instead:
```
a
```