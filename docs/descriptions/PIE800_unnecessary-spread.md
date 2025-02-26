# unnecessary-spread (PIE800)
Derived from the flake8-pie linter.
Fix is sometimes available.
## What it does
Checks for unnecessary dictionary unpacking operators (**).
## Why is this bad?
Unpacking a dictionary into another dictionary is redundant. The unpacking
operator can be removed, making the code more readable.
## Example
```
foo = {"A": 1, "B": 2}
bar = {**foo, **{"C": 3}}
```
## Use instead:
```
foo = {"A": 1, "B": 2}
bar = {**foo, "C": 3}
```