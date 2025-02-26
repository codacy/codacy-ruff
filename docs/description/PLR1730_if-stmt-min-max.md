# if-stmt-min-max (PLR1730)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for if statements that can be replaced with min() or max()
calls.
## Why is this bad?
An if statement that selects the lesser or greater of two sub-expressions
can be replaced with a min() or max() call respectively. Where possible,
prefer min() and max(), as they're more concise and readable than the
equivalent if statements.
## Example
```
if score > highest_score:
    highest_score = score
```
## Use instead:
```
highest_score = max(highest_score, score)
```