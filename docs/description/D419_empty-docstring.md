# empty-docstring (D419)
Derived from the pydocstyle linter.
## What it does
Checks for empty docstrings.
## Why is this bad?
An empty docstring is indicative of incomplete documentation. It should either
be removed or replaced with a meaningful docstring.
## Example
```
def average(values: list[float]) -> float:
    """"""
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```