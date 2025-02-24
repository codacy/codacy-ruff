# blank-line-before-function (D201)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstrings on functions that are separated by one or more blank
lines from the function definition.
## Why is this bad?
Remove any blank lines between the function definition and its docstring,
for consistency.
## Example
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```