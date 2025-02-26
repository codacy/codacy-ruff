# unnecessary-multiline-docstring (D200)
Derived from the pydocstyle linter.
Fix is sometimes available.
## What it does
Checks for single-line docstrings that are broken across multiple lines.
## Why is this bad?
PEP 257 recommends that docstrings that can fit on one line should be
formatted on a single line, for consistency and readability.
## Example
```
def average(values: list[float]) -> float:
    """
    Return the mean of the given values.
    """
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
```