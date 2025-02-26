# line-contains-xxx (FIX003)
Derived from the flake8-fixme linter.
## What it does
Checks for "XXX" comments.
## Why is this bad?
"XXX" comments are used to describe an issue that should be resolved.
Consider resolving the issue before deploying the code, or, at minimum,
using a more descriptive comment tag (e.g, "TODO").
## Example
```
def speed(distance, time):
    return distance / time  # XXX: Raises ZeroDivisionError for time = 0.
```