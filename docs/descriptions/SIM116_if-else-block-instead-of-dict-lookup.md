# if-else-block-instead-of-dict-lookup (SIM116)
Derived from the flake8-simplify linter.
## What it does
Checks for three or more consecutive if-statements with direct returns
## Why is this bad?
These can be simplified by using a dictionary
## Example
```
if x == 1:
    return "Hello"
elif x == 2:
    return "Goodbye"
else:
    return "Goodnight"
```
## Use instead:
```
return {1: "Hello", 2: "Goodbye"}.get(x, "Goodnight")
```