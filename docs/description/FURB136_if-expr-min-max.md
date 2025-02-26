# if-expr-min-max (FURB136)
Derived from the refurb linter.
Fix is sometimes available.
## What it does
Checks for if expressions that can be replaced with min() or max()
calls.
## Why is this bad?
An if expression that selects the lesser or greater of two
sub-expressions can be replaced with a min() or max() call
respectively. When possible, prefer min() and max(), as they're more
concise and readable than the equivalent if expression.
## Example
```
highest_score = score1 if score1 > score2 else score2
```
## Use instead:
```
highest_score = max(score2, score1)
```