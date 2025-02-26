# not-in-test (E713)
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for membership tests using not {element} in {collection}.
## Why is this bad?
Testing membership with {element} not in {collection} is more readable.
## Example
```
Z = not X in Y
if not X.B in Y:
    pass
```
## Use instead:
```
Z = X not in Y
if X.B not in Y:
    pass
```