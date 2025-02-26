# repeated-keyword-argument (PLE1132)
Derived from the Pylint linter.
## What it does
Checks for repeated keyword arguments in function calls.
## Why is this bad?
Python does not allow repeated keyword arguments in function calls. If a
function is called with the same keyword argument multiple times, the
interpreter will raise an exception.
## Example
```
func(1, 2, c=3, **{"c": 4})
```