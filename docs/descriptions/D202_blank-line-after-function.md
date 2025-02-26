# blank-line-after-function (D202)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstrings on functions that are separated by one or more blank
lines from the function body.
## Why is this bad?
Remove any blank lines between the function body and the function
docstring, for consistency.
## Example
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
    return sum(values) / len(values)
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
    return sum(values) / len(values)
```