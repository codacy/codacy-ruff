# needless-bool (SIM103)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for if statements that can be replaced with bool.
## Why is this bad?
if statements that return True for a truthy condition and False for
a falsy condition can be replaced with boolean casts.
## Example
```
Given:
if x > 0:
    return True
else:
    return False
```
## Use instead:
```
return x > 0
Or, given:
if x > 0:
    return True
return False
```
## Use instead:
```
return x > 0
```