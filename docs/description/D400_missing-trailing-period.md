# missing-trailing-period (D400)
Added in v0.0.68 ·
Related issues ·
View source
Derived from the pydocstyle linter.
Fix is sometimes available.
## What it does
Checks for docstrings in which the first line does not end in a period.
## Why is this bad?
PEP 257 recommends that the first line of a docstring is written in the
form of a command, ending in a period.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the numpy and
pep257 conventions, and disabled when using the google convention.
## Example
```
def average(values: list[float]) -> float:
    """Return the mean of the given values"""
```
## Use instead:
```
def average(values: list[float]) -> float:
    """Return the mean of the given values."""
Fix safety
This fix is marked as unsafe, as it may alter the intended formatting of the
docstring, or affect tools that parse docstrings and rely on specific
formatting.
```