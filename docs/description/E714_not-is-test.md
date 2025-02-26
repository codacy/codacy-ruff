# not-is-test (E714)
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for identity comparisons using not {foo} is {bar}.
## Why is this bad?
According to PEP8, testing for an object's identity with is not is more
readable.
## Example
```
if not X is Y:
    pass
Z = not X.B is Y
```
## Use instead:
```
if X is not Y:
    pass
Z = X.B is not Y
```