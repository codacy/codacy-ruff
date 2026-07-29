# comparison-of-constant (PLR0133)
Added in v0.0.221 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for comparisons between constants.
## Why is this bad?
Comparing two constants will always resolve to the same value, so the
comparison is redundant. Instead, the expression should be replaced
with the result of the comparison.
## Example
```
foo = 1 == 1
```
## Use instead:
```
foo = True
```