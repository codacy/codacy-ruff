# loop-variable-overrides-iterator (B020)
Derived from the flake8-bugbear linter.
## What it does
Checks for loop control variables that override the loop iterable.
## Why is this bad?
Loop control variables should not override the loop iterable, as this can
lead to confusing behavior.
Instead, use a distinct variable name for any loop control variables.
## Example
```
items = [1, 2, 3]
for items in items:
    print(items)
```
## Use instead:
```
items = [1, 2, 3]
for item in items:
    print(item)
```