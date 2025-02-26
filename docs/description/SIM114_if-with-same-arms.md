# if-with-same-arms (SIM114)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for if branches with identical arm bodies.
## Why is this bad?
If multiple arms of an if statement have the same body, using or
better signals the intent of the statement.
## Example
```
if x == 1:
    print("Hello")
elif x == 2:
    print("Hello")
```
## Use instead:
```
if x == 1 or x == 2:
    print("Hello")
```